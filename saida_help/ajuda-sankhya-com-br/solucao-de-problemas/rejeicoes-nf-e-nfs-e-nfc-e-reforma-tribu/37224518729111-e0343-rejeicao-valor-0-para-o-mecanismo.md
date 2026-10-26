---
id: "37224518729111"
titulo: "E0343 Rejeição: Valor 0 para o Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo tomador do serviço não é permitido na Sefin do Sistema Nacional NFS-e."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37224518729111-E0343-Rejei%C3%A7%C3%A3o-Valor-0-para-o-Mecanismo-de-apoio-fomento-ao-Com%C3%A9rcio-Exterior-utilizado-pelo-tomador-do-servi%C3%A7o-n%C3%A3o-%C3%A9-permitido-na-Sefin-do-Sistema-Nacional-NFS-e"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:16:31Z"
rotulos: ["Configuração", "SEFAZ", "NFS-e", "Regra de validação", "Erro", "Nota Fiscal de Serviço Eletrônica (NFS-e)", "Sefin do Sistema Nacional de NFS-e", "Valor informado para este mecanismo é igual a zero", "Valor 0 para o Mecanismo de apoio/fomento ao Comércio Exterior", "Mecanismo de apoio ou fomento ao Comércio Exterior", "Comércio Exterior"]
---

# E0343 Rejeição: Valor 0 para o Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo tomador do serviço não é permitido na Sefin do Sistema Nacional NFS-e.

**MENSAGEM**

E0343 Rejeição: Valor 0 para o Mecanismo de apoio/fomento ao Comércio Exterior utilizado pelo tomador do serviço não é permitido na Sefin do Sistema Nacional NFS-e.

**SITUAÇÃO**

Ao emitir uma Nota Fiscal de Serviço Eletrônica (NFS-e) no Padrão Nacional, o sistema rejeitou o documento durante a transmissão, retornando a mensagem de erro **E0343**, impedindo a autorização da nota fiscal.

**SOLUÇÃO**

Para resolver esta rejeição, siga os passos abaixo:

**(1)** Acesse a tela [**"Portal de Vendas"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654-Portal-de-Vendas) (Comercial » Consulta » Portal de Vendas) e localize a **NFS-e rejeitada**.

**(2)** Verifique as **informações relacionadas ao mecanismo de apoio/fomento ao Comércio Exterior** informadas no documento fiscal.

**(3)** Realize uma das seguintes ações:

- **Se o tomador realmente utiliza mecanismo de apoio/fomento:** Corrija o valor informado, inserindo o **valor correto e diferente de zero** para o mecanismo utilizado.
- **Se o tomador não utiliza mecanismo de apoio/fomento:** Remova a indicação de utilização do mecanismo ou deixe o campo em branco, conforme permitido pela configuração do sistema.

**(4)** Após realizar os ajustes necessários, **transmita novamente a NFS-e** para a Sefin.

**CAUSA**

A rejeição ocorre porque a **Sefin do Sistema Nacional de NFS-e** possui uma **regra de validação** que impede a transmissão de notas fiscais de serviço quando há indicação de que o tomador utiliza **mecanismo de apoio ou fomento ao Comércio Exterior**, mas o **valor informado para este mecanismo é igual a zero**. Esta validação garante a **consistência das informações fiscais**, pois se há utilização do mecanismo, deve haver um valor correspondente diferente de zero associado a ele.
