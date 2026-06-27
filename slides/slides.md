# SLIDES — Sistemas Baseados em Regras
# (copie cada bloco como um slide no Google Slides / PowerPoint)

---

## SLIDE 1 — CAPA

**SISTEMAS BASEADOS EM REGRAS**
Aplicações Inteligentes no Dia a Dia

Disciplina: Inteligência Artificial
Professor: Claudinei Dias (Ney)
2026/1

---

## SLIDE 2 — AGENDA

1. O que são Sistemas Baseados em Regras?
2. Arquitetura
3. Encadeamento para Frente e para Trás
4. Ferramentas e Frameworks
5. Casos de Uso Reais
6. Nossa Implementação
7. Demo ao Vivo
8. Conclusão

---

## SLIDE 3 — O QUE SÃO?

**Sistemas Baseados em Regras (SBR)**

São sistemas de IA que representam o conhecimento especializado na forma de regras condicionais:

> **SE** \<condição\> **ENTÃO** \<conclusão\>

**Exemplo:**
> SE paciente tem febre E tosse E perda de olfato
> ENTÃO → suspeita de COVID-19

- Também chamados de **Sistemas Especialistas**
- Reproduzem o raciocínio de um especialista humano
- Surgidos nos anos 1970 — amplamente usados até hoje

---

## SLIDE 4 — ARQUITETURA

**3 Componentes Principais:**

```
┌─────────────────┐     ┌──────────────────┐
│  Base de        │◄───►│  Motor de        │
│  Conhecimento   │     │  Inferência      │
│  (Regras)       │     │  (Raciocínio)    │
└─────────────────┘     └────────┬─────────┘
                                 │
                    ┌────────────▼─────────┐
                    │  Base de Fatos       │
                    │  (Situação Atual)    │
                    └────────────┬─────────┘
                                 │
                          ┌──────▼──────┐
                          │  Usuário    │
                          └─────────────┘
```

---

## SLIDE 5 — ENCADEAMENTO PARA FRENTE

**Forward Chaining — Orientado a Dados**

Parte dos **fatos conhecidos** → chega à **conclusão**

```
Fatos → Regra ativada → Novo fato → Regra ativada → Conclusão
```

**Exemplo:**
```
Fato: febre = true
Fato: tosse = true
Fato: perda_olfato = true
          ↓
Regra R02 disparada
          ↓
Conclusão: suspeita COVID-19
```

**Uso:** diagnóstico, monitoramento, alertas

---

## SLIDE 6 — ENCADEAMENTO PARA TRÁS

**Backward Chaining — Orientado a Objetivos**

Parte de uma **hipótese** → busca **fatos que a confirmem**

```
Hipótese → Quais regras provam isso? → Busca fatos
```

**Exemplo:**
```
Objetivo: provar "gripe"
→ Regra diz: precisamos de febre + tosse + dor de cabeça
→ Sistema pergunta: o paciente tem febre? tosse? dor de cabeça?
→ Se sim → hipótese confirmada
```

**Uso:** sistemas de diagnóstico com hipóteses pré-definidas, Prolog

---

## SLIDE 7 — FERRAMENTAS E FRAMEWORKS

| Framework | Linguagem | Destaque |
|---|---|---|
| **CLIPS** | CLIPS | NASA, anos 1980, referência histórica |
| **Drools** | Java | Mercado empresarial, bancos e seguros |
| **Experta** | Python | Port do CLIPS, prototipagem rápida |
| **PyKE** | Python | Acadêmico, suporta Prolog |

**Algoritmo central:** RETE
- Otimiza a comparação de fatos com condições das regras
- Evita reavaliação de regras que não mudaram

---

## SLIDE 8 — CASOS REAIS

**MYCIN (Stanford, 1972)**
- Diagnóstico de infecções bacterianas
- 600 regras — desempenho comparável a médicos especialistas

**XCON/R1 (DEC, 1980)**
- Configuração automática de computadores
- 2.500 regras — economizou milhões de dólares/ano

**Bancos Brasileiros (hoje)**
- Aprovação de crédito: SE score > 700 E renda > 5000 → aprovar
- Framework: Drools

**Telecomunicações (hoje)**
- Triagem de falhas antes de escalar para técnicos
- Reduz até 40% o tempo de atendimento

---

## SLIDE 9 — NOSSA IMPLEMENTAÇÃO

**Sistema Especialista de Triagem Médica Básica**
Desenvolvido em Python — sem dependências externas

- **10 regras de produção** para diagnósticos comuns
- **16 sintomas** verificados com o usuário
- **Encadeamento para frente** como motor de inferência
- **Resolução de conflitos por especificidade** (regra mais específica vence)

**Exemplo de regras:**
```python
{ "condicoes": {"febre", "tosse", "perda_de_olfato"},
  "conclusao": "Suspeita COVID-19" },

{ "condicoes": {"nausea", "vomito", "diarreia"},
  "conclusao": "Infecção intestinal" }
```

---

## SLIDE 10 — DEMO

**[DEMO AO VIVO]**

```bash
python sistema_especialista.py
```

- Usuário responde s/n para cada sintoma
- Motor de inferência avalia todas as regras
- Sistema exibe diagnóstico + regras ativadas + raciocínio usado

**Código disponível em:** GitHub do grupo

---

## SLIDE 11 — CONCLUSÃO

**Por que Sistemas Baseados em Regras ainda importam?**

✓ **Transparência** — sabe-se exatamente qual regra foi usada
✓ **Explicabilidade** — obrigatório em saúde, finanças, direito
✓ **Confiabilidade** — comportamento determinístico e auditável
✓ **Manutenção** — especialistas podem alterar regras sem programar

**Tendência:** sistemas híbridos que combinam regras (para conformidade) + ML (para adaptação)

> Regulamentações como o **AI Act europeu** exigem explicabilidade — os SBR ganham nova relevância nesse contexto.

---

## SLIDE 12 — REFERÊNCIAS

- RUSSELL; NORVIG. **Inteligência Artificial: Uma Abordagem Moderna**. GEN LTC, 2022.
- GIARRATANO; RILEY. **Expert Systems: Principles and Programming**. Course Technology, 2004.
- JACKSON, P. **Introduction to Expert Systems**. Addison-Wesley, 1999.
- NASA. **CLIPS Reference Manual**. clipsrules.net.
- RED HAT. **Drools Documentation**. drools.org.

---

*Obrigado!*
*Perguntas?*
