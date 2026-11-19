/* Deterministic two-dimensional scenes; all grounds use the shared engine. */
function heading(en, zh) {
  txt(en, 960, 205, {size:44, fam:F.disp, align:'center', c:C.white, w:700});
  txt(zh, 960, 252, {size:27, fam:F.zh, align:'center', c:C.dim});
}
function formula(s, x, y, size=43, a=1, color=C.white) {
  txt(s,x,y,{size,fam:F.math,align:'center',a,c:color});
}
function matrix2(label, rows, x, y, a=1, color=C.cyan) {
  panel(x,y,330,220,a,color);
  txt(label,x+165,y+45,{size:30,fam:F.math,align:'center',a,c:color});
  rows.forEach((row,i)=>row.forEach((v,j)=>formula(String(v),x+115+j*100,y+110+i*65,43,a)));
  txt('[',x+55,y+153,{size:100,fam:F.math,a,c:color});
  txt(']',x+263,y+153,{size:100,fam:F.math,a,c:color});
}
function block(label,x,y,w,h,color,a=1) {
  panel(x,y,w,h,a,color);
  formula(label,x+w/2,y+h/2+15,48,a,color);
}
SCENES.scalar = S => {
  badgeQ(S,[[0,null,'argued']]);
  heading('From a square to a matrix bound','从一个平方，走向矩阵界');
  formula('x² + y² − 2xy = (x − y)² ≥ 0',960,400,58);
  panel(290,480,1340,275,1,C.cyan);
  formula('XY + YX     versus     X² + Y²',960,565,55);
  txt('Compare products of eigenvalues',960,650,{size:36,fam:F.disp,align:'center',a:at(S,1,1)});
  txt('Malkoun’s question · Haobo Ma & Wenlin Zhang',960,710,{size:27,fam:F.disp,align:'center',c:C.dim,a:at(S,2,1)});
};
SCENES.example = S => {
  badgeQ(S,[[0,null,'computed']]);
  heading('Positive inputs need not give a positive Jordan product','正半定输入的混合项仍可有负特征值');
  matrix2('X',[[1,0],[0,0]],140,320);
  matrix2('Y',[[1,1],[1,1]],540,320);
  matrix2('H = XY + YX',[[2,1],[1,0]],1040,320,at(S,1,0.9),C.mag);
  matrix2('R = X² + Y²',[[3,2],[2,2]],1440,320,at(S,2,0.9));
  formula('v*Xv = |v₁|²',320,635,40);
  formula('v*Yv = |v₁+v₂|²',720,635,40);
  formula('det H = −1',1205,635,45,at(S,1,0.9),C.mag);
  formula('det R = 2',1605,635,45,at(S,2,0.9),C.cyan);
  formula('|−1| ≤ 2',960,785,62,at(S,2,1));
};
SCENES.minors = S => {
  badgeQ(S,[[0,null,'argued']]);
  heading('Choose, multiply, add','选择、相乘、相加');
  panel(140,320,740,450,1,C.cyan);
  formula('e₂(a,b,c) = ab + ac + bc',510,425,45);
  formula('e₁(λ(M)) = tr M',510,555,44,at(S,1,0.8));
  formula('eₙ(λ(M)) = det M',510,655,44,at(S,1,0.8));
  panel(990,320,790,450,1,C.mag);
  formula('eₖ(λ(M)) = Σ det M[S,S]',1385,480,42,at(S,2,1));
  txt('sum over |S| = k',1385,550,{size:30,fam:F.disp,align:'center',c:C.dim,a:at(S,2,1)});
  txt('Same row and column indices',1385,655,{size:30,fam:F.disp,align:'center',a:at(S,2,1)});
};
SCENES.stack = S => {
  badgeQ(S,[[0,null,'argued']]);
  heading('Swap the blocks; preserve the Gram matrix','交换上下两块，保持 Gram 矩阵');
  txt('U',510,330,{size:45,fam:F.math,align:'center'});
  txt('V',1410,330,{size:45,fam:F.math,align:'center'});
  block('A_S',300,365,420,155,C.cyan);
  block('B_S',300,540,420,155,C.mag);
  // V starts in the same order, then swaps deterministically during line 1.
  const swap=ease(at(S,1,1.6));
  block('A_S',1200,365+175*swap,420,155,C.cyan);
  block('B_S',1200,540-175*swap,420,155,C.mag);
  txt('2p rows · k columns · * means conjugate transpose',960,750,{size:29,fam:F.disp,align:'center',c:C.dim});
  formula('U*U = V*V = R[S,S]',960,815,42,at(S,2,0.8));
  formula('U*V = H[S,S]',960,870,42,at(S,2,0.8));
};
SCENES.gram = S => {
  badgeQ(S,[[0,null,'argued']]);
  heading('Cauchy–Schwarz acts on lists of minors','对子式列表使用 Cauchy–Schwarz');
  panel(160,320,700,190,1,C.cyan);
  panel(1060,320,700,190,1,C.mag);
  formula('u_T = det U[T,:]',510,400,44);
  formula('v_T = det V[T,:]',1410,400,44);
  formula('det(U*V) = Σ conjugate(u_T) v_T',960,580,43);
  formula('|det(U*V)|² ≤ det(U*U) det(V*V)',960,680,43,at(S,1,1));
  formula('|det H[S,S]| ≤ det R[S,S]',960,795,49,at(S,2,1));
  txt('Equal Gram matrices · nonnegative determinant',960,735,{size:29,fam:F.disp,align:'center',a:at(S,2,1),c:C.dim});
};
SCENES.sum = S => {
  badgeQ(S,[[0,null,'argued']]);
  heading('Sum the bounds, recover the spectral quantity','相加后回到特征值的对称函数');
  panel(230,320,1460,400,1,C.argued);
  formula('|eₖ(λ(H))| ≤ Σ |det H[S,S]|',960,420,50);
  formula('≤ Σ det R[S,S] = eₖ(λ(R))',960,510,50,at(S,0,1.4));
  txt('0 ≤ k ≤ n · sums over |S| = k',960,600,{size:31,fam:F.disp,align:'center',a:at(S,1,1)});
  txt('Singular matrices included · no inverses or limits',960,665,{size:29,fam:F.disp,align:'center',c:C.dim,a:at(S,1,1)});
  formula('A = X, B = Y:   |eₖ(λ(XY+YX))| ≤ eₖ(λ(X²+Y²))',960,815,39,at(S,2,1));
};
SCENES.scope = S => {
  badgeQ(S,[[0,null,'lean'],[1,null,'argued']]);
  heading('What is proved in the public Lean theorem?','公开 Lean 定理的确切范围');
  const later=at(S,1,1);
  panel(200,320,1520,225,1,C.cyan);
  txt('PSD Hermitian X,Y · n ≥ 1 · 1 ≤ k ≤ n',960,390,{size:35,fam:F.disp,align:'center'});
  formula('eₖ(λ(XY+YX)) ≤ eₖ(λ(X²+Y²))',960,475,48);
  panel(200,585,1520,225,later,C.argued);
  txt('Written proofs: absolute values and rectangular inputs',960,660,{size:32,fam:F.disp,align:'center',a:later});
  txt('Swap stacks → equal Gram matrices → sum minor bounds',960,750,{size:30,fam:F.disp,align:'center',a:at(S,2,1)});
};
FILM.poster = () => {
  heading('Swap the stacks, bound the determinant','交换堆叠，控制行列式');
  block('A_S',260,350,420,150,C.cyan);
  block('B_S',260,520,420,150,C.mag);
  block('B_S',1240,350,420,150,C.mag);
  block('A_S',1240,520,420,150,C.cyan);
  formula('U',470,740,56);
  formula('V',1450,740,56);
  formula('U*U = V*V',960,450,49);
  formula('|det H[S,S]|',960,570,39);
  formula('≤ det R[S,S]',960,630,39);
  txt('Haobo Ma · Wenlin Zhang',960,840,{size:33,fam:F.disp,align:'center',c:C.white});
  txt('Gram determinants · a written-proof mechanism',960,902,{size:28,fam:F.disp,align:'center',c:C.dim});
};
