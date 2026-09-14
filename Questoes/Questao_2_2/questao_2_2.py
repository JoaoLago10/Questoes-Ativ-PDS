"""Solução numérica e gráficos da Questão 2.2."""

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
    limite: float | None = None,
) -> None:
    """Gera e salva o gráfico de uma sequência discreta."""
    figura, eixo = plt.subplots(figsize=(8, 4.5))
    eixo.stem(n, sinal, basefmt="k-")

    if limite is not None:
        eixo.axhline(
            limite,
            color="tab:red",
            linestyle="--",
            label=f"Limite = {limite:g}",
        )
        eixo.legend()

    eixo.set(title=titulo, xlabel="n", ylabel=eixo_y)
    eixo.set_xticks(n[::2])
    eixo.grid(True, alpha=0.3)
    figura.tight_layout()
    figura.savefig(PASTA_GRAFICOS / nome_arquivo, dpi=160)
    plt.close(figura)


def main() -> None:
    """Calcula os sinais, confere a convolução e gera os gráficos."""
    n = np.arange(-5, 16)
    u = (n >= 0).astype(float)

    x = u
    h = np.where(n >= 0, 0.5**n, 0)

    # Resultado analítico: y[n] = [2 - (0,5)^n]u[n].
    y_analitica = np.where(n >= 0, 2 - 0.5**n, 0)

    # Os primeiros valores da convolução numérica devem coincidir com a
    # expressão analítica. O restante corresponde à cauda das sequências
    # truncadas e não é usado nesta conferência.
    n_causal = np.arange(0, 16)
    x_causal = np.ones_like(n_causal, dtype=float)
    h_causal = 0.5**n_causal
    y_convolucao = np.convolve(x_causal, h_causal)[: len(n_causal)]
    np.testing.assert_allclose(y_convolucao, 2 - 0.5**n_causal)

    PASTA_GRAFICOS.mkdir(parents=True, exist_ok=True)
    salvar_grafico(n, x, "Entrada: degrau unitário", "x[n]", "entrada_x.png")
    salvar_grafico(
        n,
        h,
        "Resposta ao impulso",
        "h[n]",
        "impulso_h.png",
    )
    salvar_grafico(
        n,
        y_analitica,
        "Saída do sistema",
        "y[n]",
        "saida_y.png",
        limite=2,
    )

    print("Conferência numérica concluída com sucesso.")
    print("Primeiros valores de y[n]:", y_analitica[n >= 0][:5])
    print("Soma absoluta de h[n] (valor teórico): 2")


if __name__ == "__main__":
    main()
