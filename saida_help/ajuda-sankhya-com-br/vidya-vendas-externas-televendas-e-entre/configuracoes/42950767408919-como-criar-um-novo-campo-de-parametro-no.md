---
id: "42950767408919"
titulo: "Como criar um novo campo de parâmetro no Sankhya"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950767408919-Como-criar-um-novo-campo-de-par%C3%A2metro-no-Sankhya"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Configurações"
atualizado_em: "2026-08-24T16:11:17Z"
rotulos: ["sync_hc", "vidya", "sync_hash_5bb8e3b3bcab", "vidya_600092"]
---

# Como criar um novo campo de parâmetro no Sankhya

## Objetivo

Este artigo apresenta o procedimento para **criar e disponibilizar um novo campo de parâmetro no Sankhya**, utilizando como exemplo o parâmetro **“Aplicar desconto em massa por itens”**.

O procedimento contempla desde a criação do campo na tabela de parâmetros até sua disponibilização na tela de **Configurações Vidya Force**.

---

## 1. Localizar a tabela de parâmetros

1. Acesse a tela **Construtor de Telas** no Sankhya.
2. Localize a tabela:

   **AD\_TDYCFGFRC**
3. Selecione a tabela para visualizar seus campos.

---

## 2. Criar o novo campo

Com a tabela **AD\_TDYCFGFRC** selecionada:

1. Clique no botão **"+" (Adicionar)**.
2. Preencha os dados do novo campo conforme abaixo:

| Configuração | Valor |
| --- | --- |
| **Nome do campo** | `APLICARDESCONTO` |
| **Descrição** | Aplicar desconto em massa por itens |
| **Tipo de dado** | Texto |
| **Padrão** | Checkbox |

3. Após preencher as informações, avance para a configuração dos atributos.

---

## 3. Configurar os atributos do campo

Na aba **Atributos**, configure a organização do campo na interface.

### Configurações

- **Nome da aba:** Configurações
- **Agrupamento:** Definir conforme a organização interna de **“Lançamento de Pedidos - Descontos”**.

Após realizar as configurações:

1. Revise os dados informados.
2. Clique em **Salvar**.

---

## 4. Disponibilizar o campo na tela de Configurações Vidya Force

Após a criação do campo, é necessário disponibilizá-lo na interface de configurações.

1. Acesse a tela **Configurações Vidya Force**.
2. Feche e abra novamente a aba da tela de configurações.
3. Verifique se o campo **APLICARDESCONTO** foi disponibilizado automaticamente.

### Caso o campo não apareça

Se o campo não estiver disponível:

1. Acesse a **engrenagem de Configurações** da tela.
2. Utilize a busca para localizar:

   `APLICARDESCONTO`
3. Localize o campo nos componentes disponíveis.
4. Arraste o campo para a direita, posicionando-o dentro da aba desejada.
5. Clique em **Salvar**.

---

## 5. Validar a configuração

Após salvar, confirme se:

- O campo **APLICARDESCONTO** está disponível na tela.
- A descrição apresentada está correta.
- O campo está dentro da aba **Configurações**.
- O agrupamento está de acordo com o padrão definido para **Lançamento de Pedidos - Descontos**.
- O componente está sendo apresentado como **Checkbox**.
- A configuração foi salva corretamente.

---

## Considerações técnicas

A criação de novos campos de parâmetros deve seguir a **nomenclatura padrão adotada no projeto**, evitando conflitos no dicionário de dados e facilitando a manutenção do ambiente.

Esse procedimento é utilizado para viabilizar **customizações de comportamento e configuração da jornada do usuário**, especialmente em funcionalidades relacionadas aos fluxos de vendas do Vidya Force.

> **Atenção:** antes de criar um novo campo, verifique se já existe um parâmetro com a mesma finalidade. Evite criar campos duplicados ou utilizar nomenclaturas fora do padrão definido para o ambiente.
