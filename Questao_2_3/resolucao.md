# Questão 2.3 — Sistemas em Cascata

## Dados do problema

As respostas ao impulso dos dois sistemas SLIT são

\[
h_1[n]=\delta[n]-\delta[n-1]
\]

e

\[
h_2[n]=u[n]-u[n-3].
\]

O segundo sinal é um pulso retangular de três amostras:

\[
h_2[n]=
\begin{cases}
1, & n=0,1,2,\\
0, & \text{caso contrário}.
\end{cases}
\]

## a) Resposta ao impulso equivalente

Para dois sistemas SLIT em cascata, a resposta ao impulso equivalente é a
convolução das respostas individuais:

\[
h_{eq}[n]=h_1[n]*h_2[n].
\]

Substituindo \(h_1[n]\):

\[
h_{eq}[n]
=\left(\delta[n]-\delta[n-1]\right)*h_2[n].
\]

Pela linearidade da convolução,

\[
h_{eq}[n]
=\delta[n]*h_2[n]-\delta[n-1]*h_2[n].
\]

Usando a propriedade

\[
\delta[n-n_0]*x[n]=x[n-n_0],
\]

obtém-se

\[
h_{eq}[n]=h_2[n]-h_2[n-1].
\]

Como

\[
h_2[n]=u[n]-u[n-3]
\]

e

\[
h_2[n-1]=u[n-1]-u[n-4],
\]

segue que

\[
h_{eq}[n]
=u[n]-u[n-1]-u[n-3]+u[n-4].
\]

Agrupando os termos e usando

\[
\delta[n-n_0]=u[n-n_0]-u[n-n_0-1],
\]

resulta em

\[
\boxed{h_{eq}[n]=\delta[n]-\delta[n-3]}.
\]

Em forma de sequência, considerando os índices de \(0\) a \(3\):

\[
h_1[n]=[1,-1],\qquad h_2[n]=[1,1,1]
\]

e

\[
h_{eq}[n]=[1,0,0,-1].
\]

## b) Saída para \(x[n]=\delta[n]\)

A saída do sistema equivalente é

\[
y[n]=x[n]*h_{eq}[n].
\]

Para \(x[n]=\delta[n]\):

\[
y[n]=\delta[n]*h_{eq}[n]=h_{eq}[n].
\]

Portanto,

\[
\boxed{y[n]=\delta[n]-\delta[n-3]}.
\]

Em forma de sequência:

\[
\boxed{y[n]=[1,0,0,-1],\quad 0\leq n\leq3}.
\]

## c) Comprimento da resposta ao impulso equivalente

O primeiro índice da resposta equivalente é \(n=0\), enquanto o último é
\(n=3\). Assim,

\[
L=n_{\mathrm{final}}-n_{\mathrm{inicial}}+1
  =3-0+1
  =4.
\]

O mesmo resultado é obtido pela propriedade do comprimento da convolução:

\[
L_{eq}=L_1+L_2-1=2+3-1=4.
\]

Logo,

\[
\boxed{L_{eq}=4\text{ amostras}.}
\]

Embora as amostras em \(n=1\) e \(n=2\) sejam nulas, elas estão entre os
índices inicial e final e, portanto, fazem parte do comprimento do filtro
FIR.
