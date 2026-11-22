import itertools
import json


def binary_rank(rows):
    pivots = {}
    for row in rows:
        residual = row
        while residual:
            pivot = residual.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = residual
                break
            residual ^= pivots[pivot]
    return len(pivots)


def binary_kernel(rows, column_count):
    return tuple(vector for vector in range(1 << column_count)
                 if all((row & vector).bit_count() % 2 == 0 for row in rows))


def row_space(rows):
    space = {0}
    for row in rows:
        space |= {vector ^ row for vector in tuple(space)}
    return tuple(sorted(space))


def matrix_checks():
    cases = []
    for input_count in range(4):
        for output_count in range(6):
            if input_count * output_count > 12:
                continue
            signatures = {}
            total = 0
            for rows in itertools.product(range(1 << output_count), repeat=input_count):
                profile = tuple(binary_rank([row & subset for row in rows])
                                for subset in range(1 << output_count))
                kernel = binary_kernel(rows, output_count)
                indicator = []
                for subset in range(1 << output_count):
                    supported = 1 << (subset.bit_count() - profile[subset])
                    assert supported == sum(vector & ~subset == 0 for vector in kernel)
                    proper_total = sum(indicator[proper] for proper in range(subset)
                                       if proper & ~subset == 0)
                    recovered = supported - proper_total
                    assert recovered == int(subset in kernel)
                    indicator.append(recovered)
                signature = (kernel, row_space(rows))
                assert signatures.setdefault(profile, signature) == signature
                total += 1
            cases.append({'inputs': input_count, 'outputs': output_count,
                          'matrices': total, 'distinct_profiles': len(signatures)})
    return {'range': '0 <= inputs <= 3, 0 <= outputs <= 5, inputs*outputs <= 12',
            'matrices': sum(case['matrices'] for case in cases), 'cases': cases}


class Components:
    def __init__(self, count):
        self.parent = list(range(count))

    def find(self, item):
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def join(self, first, second):
        self.parent[self.find(first)] = self.find(second)


def graph_checks():
    cases = []
    checked_moves = 0
    connectedness_checks = 0
    for vertex_count in range(6):
        edges = list(itertools.combinations(range(vertex_count), 2))
        edge_bits = {edge: 1 << index for index, edge in enumerate(edges)}
        graph_count = 1 << len(edges)
        for input_count in range(vertex_count + 1):
            output_count = vertex_count - input_count
            full_components = Components(graph_count)
            restricted_components = Components(graph_count)
            profiles = {}
            bipartite = set()

            def edge_mask(first, second):
                return edge_bits[tuple(sorted((first, second)))]

            def adjacent(graph, first, second):
                return first != second and bool(graph & edge_mask(first, second))

            def profile(graph):
                if graph not in profiles:
                    values = []
                    for subset in range(1 << output_count):
                        selected = [input_count + index for index in range(output_count)
                                    if subset >> index & 1]
                        complement = [vertex for vertex in range(vertex_count)
                                      if vertex not in selected]
                        rows = [sum(int(adjacent(graph, first, second)) << index
                                    for index, second in enumerate(complement))
                                for first in selected]
                        values.append(binary_rank(rows))
                    profiles[graph] = tuple(values)
                return profiles[graph]

            def swap_vertices(graph, first, second):
                permutation = list(range(vertex_count))
                permutation[first], permutation[second] = second, first
                return sum(edge_mask(permutation[left], permutation[right])
                           for left, right in edges if adjacent(graph, left, right))

            for graph in range(graph_count):
                is_bipartite = all(not adjacent(graph, left, right)
                                   for left, right in edges
                                   if (left < input_count) == (right < input_count))
                if is_bipartite:
                    bipartite.add(graph)
                original = profile(graph)
                for vertex in range(vertex_count):
                    changed = graph
                    neighbours = [other for other in range(vertex_count)
                                  if adjacent(graph, vertex, other)]
                    for left, right in itertools.combinations(neighbours, 2):
                        changed ^= edge_mask(left, right)
                    assert profile(changed) == original
                    full_components.join(graph, changed)
                    checked_moves += 1
                for target in range(input_count):
                    for source in range(input_count):
                        if target == source:
                            continue
                        changed = graph
                        for output in range(input_count, vertex_count):
                            if adjacent(graph, source, output):
                                changed ^= edge_mask(target, output)
                        assert profile(changed) == original
                        full_components.join(graph, changed)
                        if is_bipartite:
                            restricted_components.join(graph, changed)
                        checked_moves += 1
                for left, right in itertools.combinations(range(input_count), 2):
                    changed = graph & ~edge_mask(left, right)
                    assert profile(changed) == original
                    full_components.join(graph, changed)
                    checked_moves += 1
                for first in range(vertex_count - 1):
                    if first == input_count - 1:
                        continue
                    changed = swap_vertices(graph, first, first + 1)
                    changed_profile = profile(changed)
                    for subset in range(1 << output_count):
                        transported = subset
                        if first >= input_count:
                            output_index = first - input_count
                            if bool(subset >> output_index & 1) != bool(subset >> (output_index + 1) & 1):
                                transported ^= 3 << output_index
                        assert changed_profile[subset] == original[transported]
                    full_components.join(graph, changed)
                    if is_bipartite:
                        restricted_components.join(graph, changed)
                    checked_moves += 1
            full_to_restricted = {}
            restricted_to_full = {}
            disconnected_components = set()
            if input_count == 2:
                for graph in range(graph_count):
                    reached = {0}
                    frontier = [0]
                    while frontier:
                        vertex = frontier.pop()
                        for other in range(vertex_count):
                            if other not in reached and adjacent(graph, vertex, other):
                                reached.add(other)
                                frontier.append(other)
                    if len(reached) != vertex_count:
                        disconnected_components.add(full_components.find(graph))
            for graph in bipartite:
                full = full_components.find(graph)
                restricted = restricted_components.find(graph)
                assert full_to_restricted.setdefault(full, restricted) == restricted
                assert restricted_to_full.setdefault(restricted, full) == full
                if input_count == 2:
                    rows = [sum(int(adjacent(graph, input_index, 2 + column)) << column
                                for column in range(output_count))
                            for input_index in range(2)]
                    if binary_rank(rows) == 2:
                        types = [((rows[0] >> column) & 1) +
                                 2 * ((rows[1] >> column) & 1)
                                 for column in range(output_count)]
                        predicted = 0 not in types and all(kind in types for kind in (1, 2, 3))
                        assert predicted == (full not in disconnected_components)
                        connectedness_checks += 1
            cases.append({'inputs': input_count, 'outputs': output_count,
                          'graphs': graph_count, 'bipartite_endpoints': len(bipartite),
                          'endpoint_classes': len(full_to_restricted)})
    return {'range': 'all labelled simple graphs with inputs+outputs <= 5',
            'graphs_with_partitions': sum(case['graphs'] for case in cases),
            'checked_generator_instances': checked_moves,
            'two_input_full_rank_connectedness_checks': connectedness_checks,
            'cases': cases}


def boundary_checks():
    ternary_first = (1, 1)
    ternary_second = (1, 2)
    witness = (1, 2)
    assert sum(left * right for left, right in zip(ternary_first, witness)) % 3 == 0
    assert sum(left * right for left, right in zip(ternary_second, witness)) % 3 != 0
    assert binary_rank([1]) == binary_rank([3]) == 1
    assert binary_kernel([1], 2) != binary_kernel([3], 2)
    first_matrix = (9, 10, 4)
    second_matrix = (9, 10, 12)
    for subset in range(16):
        if subset.bit_count() <= 2:
            assert binary_rank([row & subset for row in first_matrix]) == binary_rank(
                [row & subset for row in second_matrix])
    assert binary_kernel(first_matrix, 4) == (0, 11)
    assert binary_kernel(second_matrix, 4) == (0, 15)
    return {'ternary_same_profile_different_kernels': True,
            'binary_total_rank_insufficient': True,
            'three_input_singleton_and_pair_output_cuts_insufficient': {
                'first_rows': [[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 0]],
                'second_rows': [[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]],
                'nonzero_kernel_weights': [3, 4]}}


def two_input_checks():
    changes_of_basis = [(first, second) for first in range(1, 4)
                        for second in range(1, 4) if first != second]
    cases = []
    for output_count in range(8):
        signatures = {}
        small_profiles = {}
        full_rank = 0
        connected_classes = set()
        total = 0
        for rows in itertools.product(range(1 << output_count), repeat=2):
            counts = [0, 0, 0, 0]
            for column in range(output_count):
                counts[((rows[0] >> column) & 1) +
                       2 * ((rows[1] >> column) & 1)] += 1
            signature = (counts[0], tuple(sorted(counts[1:])))
            small_profile = tuple(binary_rank([row & subset for row in rows])
                                  for subset in range(1 << output_count)
                                  if subset.bit_count() <= 2)
            assert small_profiles.setdefault(small_profile, row_space(rows)) == row_space(rows)
            orbit = []
            shared_counts = []
            edge_counts = []
            for first, second in changes_of_basis:
                transformed = []
                for coefficients in (first, second):
                    value = 0
                    for index in range(2):
                        if (coefficients >> index) & 1:
                            value ^= rows[index]
                    transformed.append(value)
                columns = tuple(sorted(((transformed[0] >> column) & 1) +
                                       2 * ((transformed[1] >> column) & 1)
                                       for column in range(output_count)))
                orbit.append(columns)
                shared_counts.append((transformed[0] & transformed[1]).bit_count())
                edge_counts.append(sum(row.bit_count() for row in transformed))
            orbit_key = min(orbit)
            assert signatures.setdefault(signature, orbit_key) == orbit_key
            assert min(shared_counts) == min(counts[1:])
            assert min(edge_counts) == output_count - counts[0] + min(counts[1:])
            assert min(shared_counts) <= (output_count - counts[0]) // 3
            if binary_rank(rows) == 2:
                full_rank += 1
                if output_count >= 4:
                    assert min(shared_counts) <= output_count // 2 - 1
                if counts[0] == 0 and min(counts[1:]) > 0:
                    connected_classes.add(tuple(sorted(counts[1:])))
            total += 1
        assert len(set(signatures.values())) == len(signatures)
        expected_connected = {(first, second, output_count - first - second)
                              for first in range(1, output_count + 1)
                              for second in range(first, output_count + 1)
                              if second <= output_count - first - second}
        assert connected_classes == expected_connected
        cases.append({'outputs': output_count, 'matrices': total,
                      'full_rank_matrices': full_rank,
                      'equivalence_classes': len(signatures),
                      'indecomposable_full_rank_classes': len(connected_classes)})
    counterexample_rows = (5, 6)
    assert binary_rank(counterexample_rows) == 2
    minima = []
    for first, second in changes_of_basis:
        transformed = []
        for coefficients in (first, second):
            transformed.append((counterexample_rows[0] if coefficients & 1 else 0) ^
                               (counterexample_rows[1] if coefficients & 2 else 0))
        minima.append((transformed[0] & transformed[1]).bit_count())
    assert minima == [1] * 6
    assert binary_kernel(counterexample_rows, 3) == (0, 7)
    for rows in itertools.product(range(8), repeat=2):
        if binary_rank(rows) == 2 and rows[0] & rows[1] == 0:
            nonzero_kernel = [vector for vector in binary_kernel(rows, 3) if vector]
            assert len(nonzero_kernel) == 1
            assert nonzero_kernel[0].bit_count() in (1, 2)
    return {'range': 'all binary 2-by-n matrices with 0 <= n <= 7',
            'matrices': sum(case['matrices'] for case in cases),
            'changes_of_basis_per_matrix': 6, 'cases': cases,
            'proposition_8_2_counterexample': {
                'rows': [[1, 0, 1], [0, 1, 1]],
                'shared_output_counts_for_all_six_bases': minima,
                'asserted_upper_bound_at_n_3': 0,
                'exact_minimum': 1,
                'nonzero_kernel_vector': [1, 1, 1],
                'no_shared_output_full_rank_forms_have_kernel_weight': [1, 2]},
            'status': 'pass'}


def main():
    result = {'schema_version': 1, 'arithmetic': 'exact integers and binary XOR',
              'matrix_checks': matrix_checks(), 'graph_checks': graph_checks(),
              'boundary_checks': boundary_checks(),
              'two_input_checks': two_input_checks(), 'status': 'pass'}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
