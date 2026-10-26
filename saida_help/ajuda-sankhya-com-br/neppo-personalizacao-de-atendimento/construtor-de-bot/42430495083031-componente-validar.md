---
id: "42430495083031"
titulo: "Componente Validar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430495083031-Componente-Validar"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:07:15Z"
rotulos: ["sync_hc", "neppo", "neppo_858000506", "sync_hash_a01dcedb6d38"]
---

# Componente Validar

O componente **Validar** verifica se um valor atende a um **tipo de validação pré-definido** (CPF, CNPJ, números etc.) e desvia o fluxo para os caminhos **válido** ou **inválido**.

---

## Visão geral

Use o Validar logo após capturar um dado do usuário (componente **Entrada de Dados**) para garantir o formato antes de seguir — evitando enviar dados inconsistentes a APIs ou cadastros.

Para formatos não cobertos pelos tipos nativos (ex.: data em padrão específico), utilize **Expressão** com regex, como mostrado no exemplo abaixo.

---

## Localização

Paleta de componentes (menu lateral direito da Área do Construtor) → categoria **Lógica** → **Validar**.

---

## Campos de configuração

| Campo | Obrigatório | Descrição | Exemplo |
| --- | --- | --- | --- |
| Valor a validar | Sim | Variável com o dado a ser verificado | `{{cpfCliente}}` |
| Tipo de validação | Sim | Tipo pré-definido: CPF, CNPJ, números, entre outros | `CPF` |
| Fluxo se válido | Sim | Destino quando o valor passa na validação, com argumentos | "Consultar Cadastro" |
| Fluxo se inválido | Sim | Destino quando o valor não passa, com argumentos | "Solicitar CPF novamente" |

---

## Comportamento

- O valor é verificado contra o tipo escolhido; o fluxo desvia para o caminho **válido** ou **inválido** conforme o resultado.
- Os desvios funcionam como nos demais componentes de decisão: cada caminho aponta para um fluxo de destino e pode levar argumentos.
- A validação de CPF/CNPJ considera o formato e os dígitos verificadores do documento (verificar na UI os tipos disponíveis e detalhes de cada um).

---

## Exemplo real de uso

Na jornada de matrícula escolar de um bot em produção, a validação de dados foi feita com o padrão alternativo **Expressão + regex** (a data de nascimento não é um tipo nativo do Validar):

1. Entrada de Dados captura `DataNascimento`.
2. Expressão avalia a regex de data e grava `"true"`/`"false"` em `resultado_data_nascimento`.
3. Expressão condicional desvia: válido → "Quero ser aluno - Ano Letivo"; inválido → "Quero ser aluno - Data Nascimento Inválida" (mensagem de erro + nova captura).

Com o componente Validar, um cenário equivalente para documento seria:

- Valor: `{{cpfResponsavel}}` (capturado por Entrada de Dados)
- Tipo: `CPF`
- Válido → fluxo "Consultar Cadastro do Responsável"
- Inválido → fluxo que envia "Ops... o CPF informado não é válido" e repete a pergunta

---

## Boas práticas e limitações

- Sempre trate o caminho **inválido** com mensagem explicativa e nova oportunidade de resposta — nunca deixe o usuário sem retorno.
- Combine com contador de tentativas para não prender o usuário em loop infinito de validação (transfira para humano após N erros).
- Para formatos fora dos tipos nativos, use **Expressão** com regex (padrão do exemplo real).
- Valide **antes** de chamar APIs com o dado — economiza requisições e evita erros de integração.
