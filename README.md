# Sistemas Baseados em Regras

Trabalho da disciplina de **Inteligência Artificial** — N3  
**Professor:** Claudinei Dias (Ney) · **Semestre:** 2026/1

---

## Sobre

Sistema Especialista de Triagem Médica desenvolvido em Python, demonstrando os conceitos de **Sistemas Baseados em Regras** com motor de inferência por **encadeamento para frente** (Forward Chaining).

O sistema analisa sintomas informados pelo usuário, aplica 10 regras de produção e apresenta o diagnóstico mais provável junto com a cadeia de inferência utilizada.

## Como executar localmente

```bash
pip install -r requirements.txt
gunicorn --chdir demo app:app
```

Acesse `http://localhost:8000` no navegador.

**Ou via Flask (dev):**

```bash
pip install flask
python demo/app.py
```

## Estrutura

```
demo/
├── sistema_especialista.py   # motor de regras + CLI
├── app.py                    # servidor Flask
└── templates/index.html      # interface web

relatorio/
└── relatorio.pdf             # relatório completo

slides/
└── Apresentação.pdf          # apresentação
```

## Integrantes

- Laíza Silva
- Jhessica Alves
- Victor Moy
