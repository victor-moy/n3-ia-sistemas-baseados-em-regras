"""
Sistema Especialista de Triagem Médica Básica
Baseado em Regras com Encadeamento para Frente (Forward Chaining)

N3 - Inteligência Artificial | Prof. Claudinei Dias
Tema: Sistemas Baseados em Regras
"""


# ─────────────────────────────────────────
#  BASE DE CONHECIMENTO
# ─────────────────────────────────────────

REGRAS = [
    {
        "id": "R01",
        "descricao": "Gripe comum",
        "condicoes": {"febre", "tosse", "dor_de_cabeca"},
        "conclusao": "DIAGNÓSTICO: Gripe comum — repouso, hidratação e antitérmico se necessário.",
    },
    {
        "id": "R02",
        "descricao": "COVID-19 (suspeita)",
        "condicoes": {"febre", "tosse", "perda_de_olfato"},
        "conclusao": "DIAGNÓSTICO: Suspeita de COVID-19 — procure um médico e faça isolamento preventivo.",
    },
    {
        "id": "R03",
        "descricao": "Infecção bacteriana respiratória",
        "condicoes": {"febre", "tosse", "dificuldade_respiratoria"},
        "conclusao": "DIAGNÓSTICO: Possível infecção bacteriana respiratória — avaliação médica urgente.",
    },
    {
        "id": "R04",
        "descricao": "Enxaqueca",
        "condicoes": {"dor_de_cabeca", "nausea", "sensibilidade_a_luz"},
        "conclusao": "DIAGNÓSTICO: Enxaqueca — repouso em ambiente escuro e analgésico específico.",
    },
    {
        "id": "R05",
        "descricao": "Infecção intestinal",
        "condicoes": {"nausea", "vomito", "diarreia"},
        "conclusao": "DIAGNÓSTICO: Infecção intestinal — hidratação oral e dieta leve.",
    },
    {
        "id": "R06",
        "descricao": "Alergia respiratória",
        "condicoes": {"espirros", "coriza", "olhos_vermelhos"},
        "conclusao": "DIAGNÓSTICO: Alergia respiratória — afaste-se do alérgeno e use anti-histamínico.",
    },
    {
        "id": "R07",
        "descricao": "Resfriado comum",
        "condicoes": {"espirros", "coriza", "tosse"},
        "conclusao": "DIAGNÓSTICO: Resfriado comum — repouso e hidratação.",
    },
    {
        "id": "R08",
        "descricao": "Hipoglicemia",
        "condicoes": {"tontura", "suor_frio", "tremores"},
        "conclusao": "DIAGNÓSTICO: Hipoglicemia — ingira algo doce imediatamente e consulte um médico.",
    },
    {
        "id": "R09",
        "descricao": "Pressão alta (suspeita)",
        "condicoes": {"dor_de_cabeca", "tontura", "visao_turva"},
        "conclusao": "DIAGNÓSTICO: Suspeita de hipertensão — meça a pressão e procure atendimento médico.",
    },
    {
        "id": "R10",
        "descricao": "Sem diagnóstico claro",
        "condicoes": set(),  # regra padrão (fallback)
        "conclusao": "DIAGNÓSTICO: Sintomas insuficientes para diagnóstico automático — consulte um médico.",
    },
]

TODOS_SINTOMAS = {
    "febre":                 "Você tem febre (temperatura acima de 37,8 °C)?",
    "tosse":                 "Você está com tosse?",
    "dor_de_cabeca":         "Você tem dor de cabeça?",
    "nausea":                "Você está com náusea?",
    "vomito":                "Você vomitou?",
    "diarreia":              "Você está com diarreia?",
    "espirros":              "Você está espirrando muito?",
    "coriza":                "Você tem coriza (nariz escorrendo)?",
    "olhos_vermelhos":       "Seus olhos estão vermelhos ou coçando?",
    "perda_de_olfato":       "Você perdeu o olfato ou paladar?",
    "dificuldade_respiratoria": "Você sente dificuldade para respirar?",
    "sensibilidade_a_luz":   "Você tem sensibilidade à luz?",
    "tontura":               "Você está sentindo tontura?",
    "suor_frio":             "Você está com suor frio?",
    "tremores":              "Você está com tremores?",
    "visao_turva":           "Sua visão está turva?",
}


# ─────────────────────────────────────────
#  MOTOR DE INFERÊNCIA — FORWARD CHAINING
# ─────────────────────────────────────────

def coletar_fatos():
    """Pergunta ao usuário sobre cada sintoma e retorna o conjunto de fatos."""
    print("\n─" * 40)
    print("  SISTEMA ESPECIALISTA DE TRIAGEM MÉDICA")
    print("─" * 40)
    print("Responda as perguntas abaixo com 's' (sim) ou 'n' (não).\n")

    fatos = set()
    for sintoma, pergunta in TODOS_SINTOMAS.items():
        while True:
            resposta = input(f"  {pergunta} [s/n]: ").strip().lower()
            if resposta in ("s", "n"):
                break
            print("  Por favor, responda 's' ou 'n'.")
        if resposta == "s":
            fatos.add(sintoma)

    return fatos


def encadeamento_para_frente(fatos):
    """
    Motor de inferência por encadeamento para frente.
    Percorre todas as regras e retorna as que têm todas as condições satisfeitas.
    Regras com mais condições satisfeitas têm prioridade.
    """
    disparadas = []

    for regra in REGRAS:
        if regra["condicoes"] and regra["condicoes"].issubset(fatos):
            disparadas.append(regra)

    # Ordena por número de condições (mais específica primeiro)
    disparadas.sort(key=lambda r: len(r["condicoes"]), reverse=True)
    return disparadas


def exibir_resultado(fatos, regras_disparadas):
    """Exibe os sintomas informados, as regras ativadas e o diagnóstico final."""
    print("\n" + "═" * 40)
    print("  RESULTADO DA ANÁLISE")
    print("═" * 40)

    print("\n► Sintomas informados:")
    if fatos:
        for s in sorted(fatos):
            print(f"   • {s.replace('_', ' ')}")
    else:
        print("   Nenhum sintoma informado.")

    print("\n► Regras disparadas:")
    if regras_disparadas:
        for r in regras_disparadas:
            conds = ", ".join(sorted(r["condicoes"])).replace("_", " ")
            print(f"   [{r['id']}] {r['descricao']} — condições: {conds}")
    else:
        print("   Nenhuma regra com todas as condições satisfeitas.")

    print("\n► Conclusão:")
    if regras_disparadas:
        # Usa a regra mais específica (maior número de condições)
        print(f"   {regras_disparadas[0]['conclusao']}")
        if len(regras_disparadas) > 1:
            print("\n   Outros diagnósticos possíveis:")
            for r in regras_disparadas[1:]:
                print(f"   • {r['conclusao']}")
    else:
        fallback = next(r for r in REGRAS if not r["condicoes"])
        print(f"   {fallback['conclusao']}")

    print("\n" + "─" * 40)
    print("  ⚠ Este sistema não substitui avaliação médica profissional.")
    print("─" * 40 + "\n")


# ─────────────────────────────────────────
#  PONTO DE ENTRADA
# ─────────────────────────────────────────

def main():
    fatos = coletar_fatos()
    regras_disparadas = encadeamento_para_frente(fatos)
    exibir_resultado(fatos, regras_disparadas)


if __name__ == "__main__":
    main()
