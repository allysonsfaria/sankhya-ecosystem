---
id: "37880819725079"
titulo: "Como gerar e enviar o S-1010 (Tabela de Rubricas)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37880819725079-Como-gerar-e-enviar-o-S-1010-Tabela-de-Rubricas"
trilha: "Manual do Produto > Pessoas+ > eSocial > Eventos de Tabela do eSocial"
atualizado_em: "2026-10-02T15:58:16Z"
rotulos: ["Configuração", "Eventos", "XML", "eSocial", "br.com.sankhya.CentraleSocial", "Central do eSocial", "Pessoal+", "Evento S-1010"]
---

# Como gerar e enviar o S-1010 (Tabela de Rubricas)

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Central do eSocial
**ID da Tela:** br.com.sankhya.CentraleSocial

---

O evento **S-1010 – Tabela de Rubricas** é utilizado para informar ao eSocial todas as **rubricas da folha de pagamento** utilizadas pela empresa, como salários, horas extras, adicionais, descontos, benefícios e encargos.

Esse evento é fundamental porque define **como cada valor da folha deve ser tratado** pelo eSocial, indicando, por exemplo:

- Se a rubrica incide em INSS, FGTS e IRRF;
- Se o valor é provento ou desconto;
- Em quais bases legais a rubrica se enquadra.

Sem o envio correto do evento S-1010, **a folha de pagamento não é validada corretamente pelo eSocial**, podendo gerar erros no fechamento da folha e no envio dos demais eventos periódicos.

### Quem está obrigado

Todas as empresas que **utilizam folha de pagamento** devem enviar o evento **S-1010**.

Isso inclui:

- Empresas do regime **Simples Nacional, Lucro Presumido e Lucro Real**;
- Pessoas físicas obrigadas ao eSocial (quando aplicável);
- Empregadores com funcionários, estagiários ou contribuintes vinculados à folha.

Sempre que existir uma rubrica utilizada na folha, ela deve estar previamente cadastrada e enviada ao eSocial por meio do S-1010.

### Prazo de envio

O evento **S-1010 deve ser enviado antes da sua utilização na folha de pagamento**.

Na prática, isso significa que:

- O evento precisa estar enviado e aceito no eSocial **antes do cálculo da folha**;
- Alterações em eventos (como incidências ou natureza) também devem ser enviadas **antes de entrarem em vigor**.

💡Sempre que um novo evento for criado ou alterado no sistema, é recomendado realizar o envio imediato ao eSocial.

### Pré-requisitos

Antes de gerar e enviar o evento S-1010, é necessário que os seguintes eventos já tenham sido enviados e estejam **com status de sucesso** no eSocial:

- **S-1000 – Informações do Empregador**
- **S-1005 – Tabela de Estabelecimentos**

Além disso, é importante verificar:

- Certificado digital válido;
- Ambiente do eSocial configurado corretamente (Produção);
- Eventos corretamente cadastrados no sistema.

### Jornada de Uso

[GIF animado: Imagem 1: Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/37961492188823)

**(1)** **Gerar o evento S-1010**

1. Acesse a **Central do eSocial** (Pessoal+ > Rotinas Folha).
2. Selecione a **Empresa** e a **Referência**.
3. Certifique de que o **Ambiente** esteja em **Produção**.
4. Clique em **Carregar**.
5. No menu lateral, escolha na opção **Geração**.
6. Clique sobre o card **Selecionar Eventos** e em seguida no evento **S-1010 – Tabela de Rubricas**.
7. Clique em **Iniciar Geração**.

**(2)**  **Enviar o evento S-1010**

1. Após a conclusão da geração, o evento S-1010 será exibido no menu **Eventos Pendentes**.
2. Clique no botão **Habilitar/Desabilitar todos** para **desabilitar todos os eventos** gerados.
3. Habilite a opção **Enviar** no card do evento **S-1010 – Tabela de Rubricas**.
4. Ative a opção **Utilizar a data de início padrão do sistema** e clique em **Enviar Dados**.
5. Acompanhe o processo de envio no menu **Eventos na Fila**.
6. Após o envio, o evento passa para o menu **Acompanhamento**, onde é possível verificar:
   - status do envio;
   - retorno do eSocial;
   - mensagens de erro ou rejeição, se houver.
7. Clique sobre o card correspondente para ver os detalhes do retorno do eSocial.

   - Em caso de erro, o sistema exibirá a mensagem retornada pelo eSocial para ajuste da rubrica.
   - Se o evento foi enviado com sucesso, será exibido o número do recibo.
8. Para visualizar os XML de envio e retorno, poderá clicar em **Baixar Arquivos** ou em **Visualizar Dados**.
