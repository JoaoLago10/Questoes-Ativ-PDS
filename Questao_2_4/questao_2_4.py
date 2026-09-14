"""Solução numérica e gráficos da Questão 2.4."""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


PASTA_GRAFICOS = Path(__file__).parent / "graficos"


def aplicar_eco(x: np.ndarray, alpha: float, atraso: int) -> np.ndarray:
    """Aplica y[n] = x[n] + alpha*x[n-atraso] a um sinal finito."""
    if atraso < 0:
        raise ValueError("O atraso deve ser um inteiro não negativo.")

    y = np.zeros(len(x) + atraso, dtype=float)
    y[: len(x)] += x
    y[atraso : atraso + len(x)] += alpha * x
    return y


def salvar_resposta_impulso(h: np.ndarray, alpha: float, atraso: int) -> None:
    """Gera o gráfico da resposta ao impulso do sistema."""
    n = np.arange(len(h))
    figura, eixo = plt.subplots(figsize=(8, 4.5))
    eixo.stem(n, h, basefmt="k-")
    eixo.axhline(0, color="black", linewidth=0.8)
    eixo.set(
        title=f"Resposta ao impulso: α={alpha:g}, D={atraso}",
        xlabel="n",
        ylabel="h[n]",
    )
    eixo.set_xticks(n)
    eixo.grid(True, alpha=0.3)
    figura.tight_layout()
    figura.savefig(PASTA_GRAFICOS / "resposta_ao_impulso.png", dpi=160)
    plt.close(figura)


def salvar_comparacao_parametros() -> None:
    """Ilustra separadamente os efeitos de alpha e do atraso D."""
    figura, eixos = plt.subplots(1, 2, figsize=(12, 4.5))

    for alpha, formato in ((0.3, "C0"), (0.8, "C1")):
        h = aplicar_eco(np.array([1.0]), alpha, atraso=5)
        eixos[0].stem(
            np.arange(len(h)),
            h,
            linefmt=f"{formato}-",
            markerfmt=f"{formato}o",
            basefmt="k-",
            label=f"α={alpha}",
        )

    for atraso, formato in ((3, "C2"), (8, "C3")):
        h = aplicar_eco(np.array([1.0]), alpha=0.6, atraso=atraso)
        eixos[1].stem(
            np.arange(len(h)),
            h,
            linefmt=f"{formato}-",
            markerfmt=f"{formato}o",
            basefmt="k-",
            label=f"D={atraso}",
        )

    eixos[0].set_title("Efeito de α com D=5")
    eixos[1].set_title("Efeito de D com α=0,6")

    for eixo in eixos:
        eixo.set(xlabel="n", ylabel="Amplitude")
        eixo.axhline(0, color="black", linewidth=0.8)
        eixo.grid(True, alpha=0.3)
        eixo.legend()

    figura.tight_layout()
    figura.savefig(PASTA_GRAFICOS / "comparacao_parametros.png", dpi=160)
    plt.close(figura)


def main() -> None:
    """Valida a expressão analítica e gera os gráficos."""
    alpha = 0.6
    atraso = 5
    impulso = np.array([1.0])

    y = aplicar_eco(impulso, alpha, atraso)
    h_esperado = np.zeros(atraso + 1)
    h_esperado[0] = 1
    h_esperado[atraso] = alpha
    np.testing.assert_allclose(y, h_esperado)

    PASTA_GRAFICOS.mkdir(parents=True, exist_ok=True)
    salvar_resposta_impulso(y, alpha, atraso)
    salvar_comparacao_parametros()

    print("Conferência numérica concluída com sucesso.")
    print("Parâmetros ilustrativos: alpha =", alpha, "e D =", atraso)
    print("h[n] =", y)
    print("Para x[n] = delta[n], y[n] = h[n].")


if __name__ == "__main__":
    main()
