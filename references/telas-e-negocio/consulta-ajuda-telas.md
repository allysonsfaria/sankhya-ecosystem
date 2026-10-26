# Consulta ao Acervo de Help e Documentação Sankhya

O ecossistema dispõe de uma base local com cerca de 10.000 artigos em Markdown extraídos do **Help Center Oficial** (`ajuda.sankhya.com.br`) e do **Portal do Desenvolvedor** (`developer.sankhya.com.br`).

---

## 1. Usando a Ferramenta de Busca Rápida (scripts/search_help.py)

Para localizar rapidamente qualquer tela, parâmetro de sistema, dúvida frequente ou especificação de API, execute o utilitário Python da skill:

### Busca Geral de Tela:
```bash
python scripts/search_help.py "parceiro" --limite 5
```

### Busca Específica por API / Developer:
```bash
python scripts/search_help.py "loadRecords" -t api -d
```

### Exibição com Detalhes e Trecho Inicial:
```bash
python scripts/search_help.py "limite de credito" -d
```

---

## 2. Estrutura dos Arquivos de Help Extraídos

Cada arquivo Markdown contém um frontmatter YAML estruturado:

```yaml
---
id: "360044594494"
titulo: "Cadastro de Parceiros"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594494-Cadastro-de-Parceiros"
trilha: "Manual do Produto > Configurações e Cadastros > Cadastros"
atualizado_em: "2026-09-28T14:12:25Z"
rotulos: ["Pedidos", "SEFAZ", "Crédito", "ACEITACGCBRANCO", "CORE_E00807", "br.com.sankhya.core.cad.parceiros"]
---
```

### Informações Valiosas no Frontmatter:
- **`rotulos`**: Lista os nomes dos parâmetros do sistema (`TSIUSU`, `TSIPAR`), códigos de erro e identificadores internos da tela.
- **`trilha`**: Caminho do menu no Sankhya OM para orientar o usuário final.
- **Seção "Parâmetros que influenciam nesta rotina"**: Descreve as flags de configuração que alteram o comportamento das validações.

---

## 3. Diretórios do Acervo Local (Autocontido na Skill)

O acervo reside dentro da própria skill em `saida_help/`, garantindo portabilidade se a pasta for movida ou transferida:

- `saida_help/ajuda-sankhya-com-br/manual-do-produto/`: Manuais completos de cada tela e rotina do sistema.
- `saida_help/ajuda-sankhya-com-br/duvidas-frequentes/`: Resoluções para mensagens de erro, parametrizações e comportamentos específicos.
- `saida_help/developer-sankhya-com-br/docs/`: Guias técnicos de arquitetura, Addon Studio e boas práticas.
- `saida_help/developer-sankhya-com-br/recipes/`: Snippets e receitas prontas em Java e HTTP.
- `saida_help/developer-sankhya-com-br/reference/`: Documentação de endpoints REST e APIs de integração.

### Atualização Periódica:
Para puxar novos artigos lançados no portal oficial, execute:
```bash
python scripts/atualizar_acervo.py
```
