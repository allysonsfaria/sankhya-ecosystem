---
id: "42950694982295"
titulo: "Cliente Prospect"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950694982295-Cliente-Prospect"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Parceiros"
atualizado_em: "2026-08-24T16:10:26Z"
rotulos: ["sync_hc", "vidya", "vidya_599872", "sync_hash_a6a6eeaaa0c0"]
---

# Cliente Prospect

## O que é um Cliente Prospect

Um **prospect** é um cliente em potencial: alguém que já demonstrou interesse no produto ou serviço, mas que ainda não fechou negócio nem possui um cadastro completo como cliente efetivo. Ele está em um estágio mais avançado do que um simples contato (lead), pois já foi identificado como uma oportunidade real de venda, mas ainda não passou pelo processo completo de qualificação e faturamento.

No Vidya Force, o **Cliente Prospect** é um tipo de cadastro simplificado que permite ao vendedor registrar rapidamente esse cliente em potencial — em campo, durante uma visita, por exemplo — sem precisar preencher de imediato todas as informações exigidas em um cadastro completo de cliente. Isso permite iniciar o relacionamento comercial (e até gerar um pedido de venda) antes de o cadastro estar 100% qualificado.

## Para que serve

- **Agilizar o cadastro em campo**: o vendedor consegue registrar um novo contato comercial rapidamente, sem travar a visita por falta de alguma informação cadastral completa.
- **Iniciar negociações antes da qualificação completa**: mesmo como prospect, o cliente já pode ser vinculado a um pedido de venda, permitindo iniciar a negociação comercial.
- **Separar cliente em potencial de cliente efetivo**: o sistema diferencia o registro de um prospect do cadastro definitivo de cliente, facilitando o acompanhamento comercial (ex.: identificar quantos prospects viraram clientes de fato).
- **Padronizar o funil comercial**: junto com os conceitos de suspect e lead, o prospect representa uma etapa organizada do funil de vendas dentro do processo comercial da empresa.

## Como habilitar o recurso

O recurso de cadastro de prospect é controlado por configurações do sistema, no módulo **Configurações Vidya Code**:

### 1. Ativar opção de cadastro de prospect?

Localizada na aba **Configurações**, seção **Cadastro de Clientes**. Quando habilitada (toggle verde), libera a opção de cadastrar um cliente como "Prospect" no aplicativo do vendedor.

### 2. Cadastra apenas prospect

Também na aba **Configurações**. Quando habilitada, força que **todo novo cadastro de cliente feito pelo app seja obrigatoriamente do tipo Prospect** — ou seja, o campo "Tipo de Cliente" já vem preenchido/travado como "Prospect", sem permitir escolher outro tipo no momento do cadastro.

> Essas duas configurações podem ser combinadas conforme a política comercial da empresa: apenas disponibilizar a opção (permitindo escolher entre cliente comum ou prospect) ou tornar o cadastro de prospect obrigatório para todo novo registro feito em campo.

## Como usar (fluxo no aplicativo do vendedor)

1. No app, acesse **Clientes** e toque em **Novo Cliente**.
2. Na aba **Dados pessoais**, selecione o **Tipo de Pessoa** (Física ou Jurídica).
3. No campo **Tipo de Cliente**, selecione **Prospect** (ou o campo já virá preenchido automaticamente, caso a configuração "Cadastra apenas prospec" esteja ativa).
4. Preencha os dados básicos solicitados (CNPJ/CPF, Nome Fantasia, Telefone, Celular, e-mail, endereço, etc.). Assim como no cadastro de cliente comum, é possível pesquisar o CNPJ para preencher os dados automaticamente e informar o estado correspondente.
5. Avance pelas abas **Adicionais** e **Perfil do Cliente**, preenchendo as informações complementares configuradas pela empresa.
6. Finalize o cadastro. O prospect passa a aparecer na carteira de clientes do vendedor, disponível para consulta e negociação.
7. A partir daí, já é possível iniciar um **pedido de venda** para esse prospect normalmente, preenchendo o cabeçalho do pedido (empresa, tipo de operação, condições de frete, tipo de negociação etc.), mesmo que o cliente ainda não tenha nenhum histórico de compras.

## Pontos de atenção

- Um cliente recém-cadastrado como prospect aparece com a marcação **"Nunca comprou"** em seu cabeçalho de pedido, já que ainda não possui histórico de vendas.
- As duas configurações (`Ativar opção de cadastro de prospect?` e `Cadastra apenas prospec`) têm efeitos diferentes — a primeira apenas **libera a opção**, a segunda **obriga** o uso do tipo Prospect em todo novo cadastro. Antes de ativar a segunda, avalie se realmente todos os cadastros feitos pelos vendedores devem nascer como prospect, ou se a equipe também precisa cadastrar clientes definitivos diretamente.
- Verifique junto ao time comercial se existe um processo definido de **conversão de prospect para cliente efetivo** (ex.: após a primeira venda ou validação cadastral completa), para manter a base organizada e evitar prospects "esquecidos" sem acompanhamento.
- Campos obrigatórios do cadastro completo de cliente continuam sendo solicitados; o prospect **não elimina** a necessidade de dados básicos, apenas viabiliza um cadastro comercial mais ágil, geralmente completado/qualificado depois.

## Resumo

| Item | Descrição |
| --- | --- |
| **O que é** | Cadastro simplificado de cliente em potencial, já qualificado como oportunidade comercial |
| **Onde configurar** | Configurações Vidya Code → aba Configurações → seção Cadastro de Clientes |
| **Configuração 1** | `Ativar opção de cadastro de prospect?` — libera a opção de tipo "Prospect" |
| **Configuração 2** | `Cadastra apenas prospec` — obriga todo novo cadastro a ser do tipo Prospect |
| **Onde usar no app** | Clientes → Novo Cliente → campo "Tipo de Cliente" = Prospect |
| **Após o cadastro** | Já é possível gerar pedido de venda para o prospect normalmente |
