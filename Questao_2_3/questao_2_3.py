"""Solução numérica e gráficos da Questão 2.3."""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


PASTA_GRAFICOS = Path(__file__).parent / "graficos"


def salvar_grafico(
    n: np.ndarray,
    sinal: np.ndarray,
    titulo: str,
    eixo_y: str,
    nome_arquivo: str,
) -> None:
    """Salva o gráfico de uma sequência discreta."""
    figura, eixo = plt.subplots(figsize=(7, 4.5))
    eixo.stem(n, sinal, basefmt="k-")
    eixo.axhline(0, color="black", linewidth=0.8)
    eixo.set(title=titulo, xlabel="n", ylabel=eixo_y)
    eixo.set_xticks(n)
    eixo.set_ylim(-1.25, 1.25)
    eixo.grid(True, alpha=0.3)
    figura.tight_layout()
    figura.savefig(PASTA_GRAFICOS / nome_arquivo, dpi=160)
    plt.close(figura)


def main() -> None:
    """Calcula a cascata, verifica o resultado e gera os gráficos."""
    # Representações causais: h1 começa em n=0 e h2 começa em n=0.
    h1 = np.array([1, -1])
    h2 = np.array([1, 1, 1])
    h_equivalente = np.convolve(h1, h2)
    resultado_esperado = np.array([1, 0, 0, -1])

    np.testing.assert_array_equal(h_equivalente, resultado_esperado)

    # A entrada é um impulso; portanto, y[n] = delta[n] * h_eq[n] = h_eq[n].
    x = np.array([1])
    y = np.convolve(x, h_equivalente)
    np.testing.assert_array_equal(y, resultado_esperado)

    PASTA_GRAFICOS.mkdir(parents=True, exist_ok=True)
    n = np.arange(-1, 5)
    h1_grafico = np.zeros_like(n)
    h2_grafico = np.zeros_like(n)
    heq_grafico = np.zeros_like(n)
    h1_grafico[(n == 0) | (n == 1)] = h1
    h2_grafico[(n >= 0) & (n <= 2)] = h2
    heq_grafico[(n >= 0) & (n <= 3)] = h_equivalente

    salvar_grafico(n, h1_grafico, "Resposta ao impulso do sistema 1", "h₁[n]", "impulso_h1.png")
    salvar_grafico(n, h2_grafico, "Resposta ao impulso do sistema 2", "h₂[n]", "impulso_h2.png")
    salvar_grafico(
        n,
        heq_grafico,
        "Resposta ao impulso equivalente",
        "h_eq[n]",
        "impulso_equivalente.png",
    )

    print("Conferência numérica concluída com sucesso.")
    print("h_eq[n] =", h_equivalente)
    print("y[n]    =", y)
    print("Comprimento de h_eq[n] =", len(h_equivalente))


if __name__ == "__main__":
    main()
