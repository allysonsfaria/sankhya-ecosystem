---
id: "https://developer.sankhya.com.br/reference/mapeamento-de-serviço"
titulo: "Mapeamento de serviços"
url: "https://developer.sankhya.com.br/reference/mapeamento-de-serviço"
atualizado_em: "2025-11-10T23:39:01.000Z"
---

# Mapeamento de serviços

Em função da imensa quantidade de serviços existentes na plataforma Sankhya, nem todos estão documentados, entretanto é possível identificá-los através da ferramenta de desenvolvimento do navegador (no Google Chrome, DevTools) Confira neste artigo o procedimento de localização e nossa seleção de serviços que podem ser úteis no dia a dia do seu desenvolvimento.

## Procedimento

1. Abra a **tela** que executa o serviço que você deseja chamar via API
2. Entre na ferramenta de desenvolvimento do navegador **DevTools** (f12)
3. Realize a operação na tela de chamada de serviços (Click no Botão)
4. Navegue até a aba de **Network** do DevTools.
5. Filtre os resultados por **"service.sbr"**
6. Na chamada do serviço, o requestbody (SubAba Payload) e o response serão obtidos
7. Copie a chamada
8. Utilize o serviço

<HTMLBlock>{`
<iframe width="560" height="315" src="https://drive.google.com/file/d/1I5FeqArUVnH1Qx-vtAUvXJxuvk3HXheU/preview" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
`}</HTMLBlock>

> 📘 Informação Importante
>
> Na central de ajuda da Sankhya também está disponível uma documentação que auxilia na identificação dos serviços nativos do ERP, os parâmetros da requisição do serviço além da identificação de dados da resposta. Para acessa-lo, [clique aqui](https://ajuda.sankhya.com.br/hc/pt-br/articles/4403903691799-Tarefas-de-Servi%C3%A7o-com-Web-Service-Interno#configurandotarefadeservi%C3%A7ocomwebserviceinterno).

## Lista de serviços úteis

Confira abaixo uma lista de serviços habitualmente utilizados, através da tela e do botão descrito basta seguir o procedimento e para utilização

* **Serviço:**&#x41;diantamentoEmprestimoSP.gerarAdiantamentoEmprestimo\
  **Tela:** Adiantamento/Empréstimo\
  **botão:** Cria um novo adiantamento/empréstimo.

* **Serviço:** AdiantamentoEmprestimoSP.salvarParcelamento\
  **tela:** Adiantamento/Empréstimo\
  **Botão:** Confirmar

* **Serviço:** AdiantamentoEmprestimoSP.desfazerAdiantamento\
  **Tela:** Adiantamento/Empréstimo\
  **Botão:** Remove um adiantamento/empréstimo já confirmado.

* **Serviço:** BaixaFinanceiroSP.montaDadosBaixa\
  **Tela:** Movimentação Financeira\
  **Botão:** Baixar

* **Serviço:** BaixaFinanceiroSP.baixarTitulo\
  **Tela:** Movimentação Financeira\
  **Botão:** Baixar

* **Serviço:** BaixaFinanceiroSP.estornarTitulo\
  **Tela:** Movimentação Financeira\
  **Botão:** Estornar

* **Serviço:** BaixaFinanceiroSP.estornarMultiplosTitulos\
  **Tela:** Movimentação Financeira\
  **Botão:** Estornar

* **Serviço: ContaBancariaSP.getSaldosBancoNaReferencia**\
  **Tela:** Contas - Aba Saldos\
  **Botão:** refresh na tela

* **Serviço: ContaBancariaSP.corrigirSaldoBanco**\
  **Tela:** Contas - Aba Saldos\
  **Botão:** Corrigir Saldo Banco

* **Serviço: ContaBancariaSP.getInfoSaldo**\
  **Tela:** Contas - popup de Implanta Saldo de Contas\
  **Botão:** Referência p/ Aceitar Lançamentos

## Como tirar dúvidas?

Para tirar dúvidas e compartilhar informações, use a [Comunidade Sankhya Developers](https://community.sankhya.com.br/developers).

<br />

## Links Úteis

<HTMLBlock>{`
<p style="text-align:left"><a href="https://ajuda.sankhya.com.br/hc/pt-br/articles/360050259413-Sankhya-ID" target="_blank">SankhyaID</a> | <a href="https://developer.sankhya.com.br/reference/api-de-integra%C3%A7%C3%B5es-sankhya">Documenta&ccedil;&atilde;o da API</a> | <a href="https://ajuda.sankhya.com.br/hc/pt-br/articles/10007620733463-Configura%C3%A7%C3%B5es-Gateway" target="_blank">Libera&ccedil;&atilde;o de Ambientes/Gerar Token</a> |<br /> <a href="https://developer.sankhya.com.br/reference/mapeamento-de-servi%C3%A7o">Como Mapear Servi&ccedil;os</a>
<a href="https://developer.sankhya.com.br/reference/boas-pr%C3%A1ticas-para-integra%C3%A7%C3%A3o">Boas Pr&aacute;ticas de Integra&ccedil;&atilde;o</a> | <a href="https://status-gateway.sankhya.com.br/" target="_blank">Status do Gateway</a> | <a href="https://developer.sankhya.com.br/docs/tech-academy-sankhya" target="_blank">Artigos Sankhya</a> | <br /> <a href="https://community.sankhya.com.br/developers" target="_blank">Comunidade para D&uacute;vidas</a></p>
`}</HTMLBlock>
