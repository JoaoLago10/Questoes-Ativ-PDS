# Questão 2.2 — Resposta ao Degrau e Estabilidade

## Dados do problema

O sistema é SLIT e possui resposta ao impulso

\[
h[n]=(0{,}5)^n u[n].
\]

A entrada é o degrau unitário

\[
x[n]=u[n].
\]

## a) Saída pela soma de convolução

Para um sistema SLIT, a saída é dada pela convolução entre a entrada e a
resposta ao impulso:

\[
y[n]=x[n]*h[n]
    =\sum_{k=-\infty}^{\infty}x[k]h[n-k].
\]

Substituindo os sinais fornecidos:

\[
y[n]=\sum_{k=-\infty}^{\infty}
u[k](0{,}5)^{n-k}u[n-k].
\]

Os degraus determinam os valores de \(k\) para os quais há sobreposição:

\[
u[k]\neq 0 \Rightarrow k\geq 0,
\qquad
u[n-k]\neq 0 \Rightarrow k\leq n.
\]

Consequentemente, para \(n\geq 0\), os limites são \(0\leq k\leq n\).
Para \(n<0\), não existe sobreposição e a saída é nula. Assim,

\[
y[n]=\sum_{k=0}^{n}(0{,}5)^{n-k},\qquad n\geq 0.
\]

Fazendo \(j=n-k\), obtém-se:

\[
y[n]=\sum_{j=0}^{n}(0{,}5)^j.
\]

Essa é uma série geométrica finita. Usando

\[
\sum_{j=0}^{n}r^j=\frac{1-r^{n+1}}{1-r},
\]

segue que

\[
y[n]
=\frac{1-(0{,}5)^{n+1}}{1-0{,}5}
=2\left[1-(0{,}5)^{n+1}\right]
=2-(0{,}5)^n,
\qquad n\geq 0.
\]

Portanto, a saída em forma fechada é

\[
\boxed{y[n]=\left[2-(0{,}5)^n\right]u[n]}.
\]

Como conferência, \(y[0]=1\), \(y[1]=1{,}5\), \(y[2]=1{,}75\), e a
saída tende a \(2\) quando \(n\) tende ao infinito.

## b) Estabilidade BIBO

Um sistema SLIT discreto é BIBO estável se, e somente se, sua resposta ao
impulso for absolutamente somável:

\[
\sum_{n=-\infty}^{\infty}|h[n]|<\infty.
\]

Como \(h[n]=(0{,}5)^n u[n]\), tem-se

\[
\sum_{n=-\infty}^{\infty}|h[n]|
=\sum_{n=0}^{\infty}|(0{,}5)^n|
=\sum_{n=0}^{\infty}(0{,}5)^n.
\]

Essa série geométrica possui razão \(0{,}5\), cujo módulo é menor que
um. Portanto, ela converge e sua soma é

\[
\sum_{n=0}^{\infty}(0{,}5)^n
=\frac{1}{1-0{,}5}
=2<\infty.
\]

Logo,

\[
\boxed{\text{o sistema é BIBO estável}.}
\]

Os gráficos gerados pelo arquivo `questao_2_2.py` servem como verificação
visual da entrada, da resposta ao impulso e da saída, mas as conclusões
acima decorrem das demonstrações analíticas.
