---
id: "35111803823383"
titulo: "Processo de Importação de arquivos nos cadastros de alíquotas (IBS, CBS e IS)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/35111803823383-Processo-de-Importa%C3%A7%C3%A3o-de-arquivos-nos-cadastros-de-al%C3%ADquotas-IBS-CBS-e-IS"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Importação de documentos fiscais"
atualizado_em: "2026-08-19T13:19:58Z"
rotulos: ["Configuração", "Fiscal", "Alíquota de ISS", "Importação", "Impostos", "Alíquotas de CBS", "Alíquotas de IBS"]
---

# Processo de Importação de arquivos nos cadastros de alíquotas (IBS, CBS e IS)

**Você encontra neste artigo:**

| [O que é e para que serve](https://ajuda.sankhya.com.br/hc/pt-br/articles/35111803823383-Processo-de-Importa%C3%A7%C3%A3o-de-arquivos-nos-cadastros-de-al%C3%ADquotas-IBS-CBS-e-IS#oqueepara) [Antes de começar](https://ajuda.sankhya.com.br/hc/pt-br/articles/35111803823383-Processo-de-Importa%C3%A7%C3%A3o-de-arquivos-nos-cadastros-de-al%C3%ADquotas-IBS-CBS-e-IS#antesdecomecar) [Etapa 1 — Baixar a planilha modelo](https://ajuda.sankhya.com.br/hc/pt-br/articles/35111803823383-Processo-de-Importa%C3%A7%C3%A3o-de-arquivos-nos-cadastros-de-al%C3%ADquotas-IBS-CBS-e-IS#baixar-modelo) [Etapa 2 — Preencher a planilha](https://ajuda.sankhya.com.br/hc/pt-br/articles/35111803823383-Processo-de-Importa%C3%A7%C3%A3o-de-arquivos-nos-cadastros-de-al%C3%ADquotas-IBS-CBS-e-IS#preencher) | [Etapa 3 — Importar os cadastros](https://ajuda.sankhya.com.br/hc/pt-br/articles/35111803823383-Processo-de-Importa%C3%A7%C3%A3o-de-arquivos-nos-cadastros-de-al%C3%ADquotas-IBS-CBS-e-IS#importar) [Etapa 4 — Acompanhar o processamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/35111803823383-Processo-de-Importa%C3%A7%C3%A3o-de-arquivos-nos-cadastros-de-al%C3%ADquotas-IBS-CBS-e-IS#acompanhar) [Histórico de importações](https://ajuda.sankhya.com.br/hc/pt-br/articles/35111803823383-Processo-de-Importa%C3%A7%C3%A3o-de-arquivos-nos-cadastros-de-al%C3%ADquotas-IBS-CBS-e-IS#historico) |
| --- | --- |

**Módulo:** Fiscal
**Caminho de acesso:** Menu Principal › Cadastros › Alíquotas de IS/CBS/IBS
**Versão mínima:** 5.17.0 (Módulo Livros Fiscais)

---

## O que é e para que serve

A rotina **Importar Cadastros** permite incluir e atualizar registros de alíquotas de IBS, CBS e IS em massa, a partir de planilhas no formato `.xlsx`. Use-a quando o volume de alíquotas a cadastrar ou atualizar tornar o preenchimento manual inviável. O processo pode ser acompanhado diretamente na tela de cada imposto e roda em segundo plano, sem bloquear o uso do sistema. A rotina não realiza lançamentos fiscais nem calcula impostos — ela apenas cria ou atualiza os registros de alíquota.

---

## Antes de começar

- Utilize sempre a planilha modelo disponível na própria tela — o sistema bloqueia importações feitas com modelos desatualizados ou incorretos.
- Para os campos **Finalidade da Operação** e **Empresa** que usam cadastro genérico, verifique se o **código 0** (padrão) já existe na sua base antes de importar.
- Confirme que está na tela do imposto correto antes de subir o arquivo: importar uma planilha de CBS na tela de IBS, por exemplo, será bloqueado pelo sistema.

**⚠️ Atenção**

O modelo de planilha foi atualizado em 12/2025 para incluir todos os novos campos exigidos nas alíquotas de IBS, CBS e IS conforme a legislação da Reforma Tributária. Baixe sempre o modelo mais recente diretamente da tela — modelos anteriores serão rejeitados na importação.

---

## Etapa 1 — Baixar a planilha modelo

1. Acesse a tela do imposto desejado: **Alíquotas de IBS**, **Alíquotas de CBS** ou **Alíquotas de IS**.
2. Clique em **Mais Opções** e selecione **Baixar Planilha Modelo**.
3. Salve o arquivo `.xlsx` no seu computador.

A planilha já vem com as colunas obrigatórias de cada tipo de alíquota preenchidas e formatadas.

![Imagem 1: A planilha já vem com as colunas obrigatórias de cada tipo de alíquota preenchidas e formatadas.](https://ajuda.sankhya.com.br/hc/article_attachments/41087150721559)

---

## Etapa 2 — Preencher a planilha

1. Abra o arquivo modelo.
2. Preencha as informações de acordo com cada coluna — preencha todas as colunas obrigatórias.
3. Use apenas o layout fornecido — não altere cabeçalhos, ordem das colunas nem adicione colunas extras.

Atenção aos seguintes pontos ao preencher:

**Formato dos campos fiscais**

Os campos **NCM**, **NBS**, **CNAE**, **CST** e **Classificação Tributária** estão configurados no formato **Texto**. Se você editar a planilha em um programa diferente, confirme que esses campos continuam como **Texto** antes de importar. Se estiverem como **Número**, zeros à esquerda podem desaparecer e causar erros na importação.

**Regime Tributário**

Preencha o campo **Regime Tributário** com o código correspondente — não com o nome por extenso:

| Código | Regime Tributário |
| --- | --- |
| **0** | Sem Regime Tributário |
| **1** | Simples Nacional |
| **2** | Simples Nacional - Sublimite |
| **3** | Regime Normal |

**Cadastro genérico (código 0)**

Para os campos **Finalidade da Operação** e **Empresa** que usam cadastro genérico, o **código 0** precisa existir na base antes da importação. Verifique isso antes de subir o arquivo.

**💡 Dica**

Para entender o contexto legislativo dos campos que você está preenchendo, acesse o [Glossário de Termos Técnicos Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/35013013220887-Gloss%C3%A1rio-de-Termos-T%C3%A9cnicos-Fiscais), o [Guia Reforma Tributária](https://www.sankhya.com.br/guia-reforma-tributaria/#introducao) e a [Seção Reforma Tributária](https://ajuda.sankhya.com.br/hc/pt-br/categories/34702076010775-Reforma-tribut%C3%A1ria) na Central de Ajuda.

---

## Etapa 3 — Importar os cadastros

1. Na tela de Cadastro de Alíquotas, clique em **Mais Opções** e selecione **Importar Cadastros**.
2. Arraste o arquivo `.xlsx` para a área indicada ou clique para selecionar o arquivo. O sistema aceita apenas o formato `.xlsx` e avisa imediatamente sobre qualquer incompatibilidade.
3. Confirme a importação.
   - Se a planilha não corresponder ao tipo de alíquota em edição, o sistema exibirá uma mensagem informando o erro.
   - Se uma planilha de um imposto diferente for anexada (por exemplo, planilha de CBS na tela de IBS), o sistema bloqueia a importação e exibe uma mensagem informando o tipo de alíquota esperado.
4. Revise os dados exibidos e clique em **Processar**.

Durante o processamento, o sistema executa automaticamente as seguintes validações:

- Organização dos dados e validação fiscal.
- Verificação do formato do NCM.
- Confirmação de que NCM e NBS não estão preenchidos para o mesmo item.

Ao final, você recebe uma confirmação de sucesso ou um relatório indicando quais linhas da planilha precisam de ajuste.

---

## Etapa 4 — Acompanhar o processamento

- O sistema processa a importação em **segundo plano** — você pode continuar usando o Sankhya Om normalmente.
- Se fechar e reabrir a tela, o status do processamento será exibido até a conclusão.

---

## Histórico de importações

Na tela de importação, você pode visualizar uma lista de todas as importações anteriores, com as seguintes informações para cada registro:

- Data e hora da importação.
- Usuário que realizou a importação.
- Status: sucesso, falha ou em processamento.
