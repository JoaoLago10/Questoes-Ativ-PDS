# Questão 2.4 — Modelagem de Eco em Áudio

## Dados do problema

O sistema de áudio discreto é descrito por

\[
y[n]=x[n]+\alpha x[n-D],
\]

em que \(\alpha\) é o ganho do eco e \(D\) é o atraso, em amostras.
Para representar um eco, considera-se \(D\) inteiro e positivo.

## a) Resposta ao impulso

Pela propriedade de deslocamento do impulso,

\[
x[n]*\delta[n]=x[n]
\]

e

\[
x[n]*\delta[n-D]=x[n-D].
\]

Portanto, a equação do sistema pode ser escrita como

\[
y[n]
=x[n]*\delta[n]+\alpha x[n]*\delta[n-D].
\]

Aplicando a propriedade distributiva:

\[
y[n]
=x[n]*\left(\delta[n]+\alpha\delta[n-D]\right).
\]

Comparando essa expressão com a relação geral de um sistema SLIT,

\[
y[n]=x[n]*h[n],
\]

obtém-se:

\[
\boxed{h[n]=\delta[n]+\alpha\delta[n-D]}.
\]

Essa resposta possui um impulso de amplitude \(1\) em \(n=0\), associado
ao som original, e outro de amplitude \(\alpha\) em \(n=D\), associado ao
eco.

## b) Saída para \(x[n]=\delta[n]\)

Substituindo a entrada impulso na equação do sistema:

\[
y[n]=\delta[n]+\alpha\delta[n-D].
\]

De forma equivalente, pela convolução:

\[
y[n]=\delta[n]*h[n]=h[n].
\]

Logo,

\[
\boxed{y[n]=\delta[n]+\alpha\delta[n-D]}.
\]

Como esperado para qualquer sistema SLIT, sua saída para uma entrada
impulso é a própria resposta ao impulso.

## c) Impacto dos parâmetros \(\alpha\) e \(D\)

### Efeito de \(\alpha\)

O parâmetro \(\alpha\) multiplica a cópia atrasada e determina sua
amplitude:

- \(\alpha=0\): não existe eco;
- \(0<|\alpha|<1\): o eco é mais fraco que o áudio original;
- quanto maior for \(|\alpha|\), mais forte e perceptível será o eco;
- \(\alpha<0\): além do atraso, ocorre inversão de sinal;
- \(|\alpha|>1\): o eco possui amplitude maior que o som original.

Se \(\alpha\) for denominado coeficiente de atenuação, é importante notar
que aumentar seu valor numérico causa **menor atenuação** e, portanto, um
eco mais forte. Já aumentar uma atenuação expressa em decibéis causaria o
efeito contrário.

### Efeito de \(D\)

O parâmetro \(D\) determina quantas amostras separam o áudio original de
sua cópia:

- \(D\) pequeno: o eco fica muito próximo do som original e pode ser
  percebido como reforço, coloração ou reverberação curta;
- \(D\) grande: o eco fica temporalmente separado e é percebido como uma
  repetição distinta.

Se a frequência de amostragem for \(f_s\), o atraso em segundos é

\[
\boxed{T_{\mathrm{eco}}=\frac{D}{f_s}}.
\]

Por exemplo, para \(f_s=44\,100\ \text{Hz}\) e \(D=4\,410\) amostras:

\[
T_{\mathrm{eco}}=\frac{4\,410}{44\,100}=0{,}1\ \text{s}.
\]

## Observação sobre estabilidade

Embora não seja solicitado, o sistema possui resposta ao impulso finita.
Para qualquer \(\alpha\) finito:

\[
\sum_{n=-\infty}^{\infty}|h[n]|=1+|\alpha|<\infty.
\]

Consequentemente, esse sistema de eco simples é BIBO estável.
