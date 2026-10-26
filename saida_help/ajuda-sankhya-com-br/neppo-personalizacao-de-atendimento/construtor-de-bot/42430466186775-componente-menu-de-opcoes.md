---
id: "42430466186775"
titulo: "Componente Menu de Opções"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430466186775-Componente-Menu-de-Op%C3%A7%C3%B5es"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:07:04Z"
rotulos: ["sync_hc", "neppo", "neppo_858000358", "sync_hash_16eb89551434"]
---

# Componente Menu de Opções

O componente **Menu de Opções** apresenta uma lista de opções ao usuário e **desvia o fluxo conforme a escolha**. É o principal componente de navegação dos bots: cada opção aponta para um fluxo de destino e pode enviar argumentos (variáveis) junto.

---

## Visão geral

Existem dois modos de exibição:

- **Menu Padrão** — opções numeradas em texto simples, compatível com qualquer canal. Cada opção pode ter "palavras semelhantes" (sinônimos aceitos como resposta).
- **Mensagem Interativa** — exclusivo do **WhatsApp**, nos formatos:

  - **Botão**: até **3 botões**, com no máximo **20 caracteres** por opção; cabeçalho e rodapé opcionais.
  - **Lista**: até **10 opções** (máx. 20 caracteres cada), agrupadas em seções com título (mínimo 1 seção), abertas por **1 botão** de abertura (ex.: "Ver opções").

---

## Localização

Paleta de componentes (menu lateral direito da Área do Construtor) → categoria **Elementos** → **Menu de Opções** (também marcado com a tag **WhatsApp** no modo interativo).

---

## Campos de configuração

| Campo | Obrigatório | Descrição | Exemplo |
| --- | --- | --- | --- |
| Tipo de menu | Sim | Menu Padrão ou Mensagem Interativa (Botão / Lista) | Lista |
| Texto do corpo (mensagem) | Sim | Texto exibido acima das opções. Aceita `{{variavel}}` | `Selecione o ano letivo pretendido:` |
| Cabeçalho | Não | Cabeçalho da mensagem interativa (texto ou imagem) | — |
| Rodapé | Não | Texto de rodapé da mensagem interativa | — |
| Título do botão de abertura | Sim (modo Lista) | Rótulo do botão que abre a lista | `Ver opções` |
| Seções e opções | Sim | Título da seção (Lista) e, por opção: texto (máx. 20 caracteres), descrição, fluxo de destino e argumentos | Opção `2025` → fluxo "Menu Cursos" com `{"AnoLetivo": "2025"}` |
| Palavras semelhantes | Não (Menu Padrão) | Sinônimos aceitos para cada opção | `["um", "primeiro"]` para a opção 1 |
| Variável de armazenamento | Sim | Variável que recebe a resposta escolhida | `AnoLetivo` |
| Opção padrão (else) | Sim (recomendado) | Fluxo executado quando a resposta não corresponde a nenhuma opção | Reexibir o próprio menu ou fluxo de tratativa |
| Inatividade | Não | Fluxo executado se o usuário não responder no tempo configurado | — |

---

## Comportamento

- O componente envia o menu e **aguarda a resposta** do usuário; a escolha é gravada na variável configurada.
- Cada opção desvia para o **fluxo de destino** configurado, levando os **argumentos** definidos — é assim que as variáveis coletadas são propagadas pela jornada.
- Respostas que não correspondem a nenhuma opção (nem às palavras semelhantes) caem na **opção padrão (else)**.
- Internamente, o componente gera um grupo de ações `message` + `receive` + `menu`: a mensagem exibe o menu, o `receive` captura a resposta na variável e o `menu` resolve o desvio.
- Em canais que não suportam mensagem interativa, utilize o Menu Padrão.

---

## Exemplo real de uso

Na jornada de matrícula escolar de um bot em produção:

**Modo Botão** (fluxo "Quero ser aluno - Ano Letivo") — 3 botões, respeitando o limite do WhatsApp:

- Corpo: `Excelente! Agora {{contact.displayName}} favor selecionar o ano letivo pretendido:`
- Botões: `2025`, `2026`, `2027` — todos desviam para "Menu Cursos", enviando `{"NomeAluno": "{{NomeAluno}}", "DataNascimento": "{{DataNascimento}}", "AnoLetivo": "2025"}` (com o ano correspondente).
- Else: reexibe o próprio menu.

**Modo Lista** (fluxo "Menu Principal") — botão de abertura "Ver opções", seção "Menu de opções" com as opções `Quero ser Portal`, `Sou Portal`, `Trabalhe conosco💼`, `Fornecedor`, cada uma desviando para "Verificar Horário de Atendimento" com argumentos `{"name": "serportal", "attempts": "0"}` etc.

**Opção padrão em ação** (fluxo "[Funções] Renderizar Menu"): quando o usuário responde algo inválido, o else redireciona para um fluxo que incrementa a variável `attempts` e reexibe o menu; após 3 tentativas, o atendimento é transferido para um grupo humano.

---

## Boas práticas e limitações

- **Limites do WhatsApp**: Botão = máx. 3 opções; Lista = máx. 10 opções; **20 caracteres por opção** — textos maiores são cortados ou rejeitados.
- Sempre configure a **opção padrão (else)**; sem ela, respostas inválidas deixam o usuário sem retorno.
- Implemente **contador de tentativas** (padrão `attempts`) e transfira para atendimento humano após N respostas inválidas.
- Repasse **todas as variáveis já coletadas** nos argumentos de cada opção — o fluxo de destino não enxerga variáveis locais do fluxo anterior.
- No Menu Padrão, cadastre **palavras semelhantes** para melhorar o reconhecimento de respostas digitadas.
- Use o corpo do menu para resumir dados e pedir confirmação (padrão "Confirmar Dados" com botões Sim/Não).
