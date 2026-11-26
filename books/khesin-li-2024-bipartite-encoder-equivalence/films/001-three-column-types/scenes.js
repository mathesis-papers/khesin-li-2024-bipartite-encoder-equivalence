'use strict';

function centered(label, x, y, size, colour, opacity = 1) {
  txt(label, x, y, { size, fam: F.mono, w: 700, align: 'center', c: colour, a: opacity });
}

function heading(titleZh, titleEn) {
  centered(titleEn, W / 2, H * 0.19, 54, C.white);
  txt(titleZh, W / 2, H * 0.26, { size: 34, fam: F.zh, align: 'center', c: C.cyan });
}

function column(x, upper, lower, shared, opacity = 1) {
  const colour = shared ? C.now : C.cyan;
  panel(x - 123, H * 0.32, 246, H * 0.37, opacity, colour, shared ? 'SHARED' : 'OUTPUT');
  centered(upper, x, H * 0.49, 78, colour, opacity);
  centered(lower, x, H * 0.62, 78, colour, opacity);
}

SCENES.open = scene => {
  heading('共享列可以换位', 'A shared output moves');
  const switched = at(scene, 2, 0.6);
  column(W * 0.30, '1', '0', false);
  column(W * 0.50, switched >= 0.5 ? '1' : '0', '1', switched >= 0.5);
  column(W * 0.70, switched >= 0.5 ? '0' : '1', '1', switched < 0.5);
  centered('row 1 ← row 1 + row 2  (mod 2)', W / 2, H * 0.77, 38, C.white, switched);
};

SCENES.types = scene => {
  heading('三种非零列始终不同', 'Three distinct nonzero types');
  column(W * 0.30, '1', '0', false);
  column(W * 0.50, '0', '1', false);
  column(W * 0.70, '1', '1', true);
  centered('Reversible changes permute types; 00 stays 00.', W / 2, H * 0.76, 34, C.white, at(scene, 1, 0.5));
  centered('Bipartite endpoints → rows and permutations suffice', W / 2, H * 0.82, 30, C.cyan, at(scene, 2, 0.5));
};

SCENES.close = scene => {
  heading('让最少的一类成为共享列', 'Choose the rarest type');
  const example = at(scene, 1, 0.6);
  centered('Counts:   a        b        c', W / 2, H * 0.40, 48, C.cyan);
  centered('minimum shared = min(a, b, c)', W / 2, H * 0.51, 50, C.white);
  centered('a = b = c = 1  ⇒  minimum = 1', W / 2, H * 0.66, 54, C.now, example);
  centered('Decoration-free graph moves only', W / 2, H * 0.77, 32, C.white, at(scene, 2, 0.5));
};
