---
id: "360053811873"
titulo: "Devolução de IPI por indústria ou equiparada"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360053811873-Devolu%C3%A7%C3%A3o-de-IPI-por-ind%C3%BAstria-ou-equiparada"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T14:00:35Z"
rotulos: ["Configuração", "Devolução de Compra", "NF-e", "Compra", "IPI", "Impostos", "TOP", "Devolução", "Indústria", "equiparada", "nota fiscal"]
---

# Devolução de IPI por indústria ou equiparada

Frequentemente, ocorrem situações em que uma empresa industrial adquire produtos de um fornecedor que também é uma indústria e, portanto, trabalha com IPI; ao realizar uma operação de Devolução de Compra, deve-se também devolver o IPI a este fornecedor.

No Sankhya Om, podemos realizar este procedimento de Devolução de Compra, onde teremos o seguinte comportamento:

- No XML da Devolução não será enviado o valor do IPI através da tag **<vIPI>**;
- Na Devolução da Nota de Compra, os valores para o IPI é o **"Vlr. IPI"**; os campos **"Base do IPI"** e **"Alíq. IPI"** estarão informados;
- No XML da Devolução não irá conter o Grupo de IPI.

Na Devolução de Compra emitida por indústria ou equiparada, para que seja informado o valor do IPI na tag **<vIPIDevol>**, são necessárias algumas configurações na TOP de Devolução:

- O **"Tipo Movimento"** da TOP deve ser **"E-Devolução de compra"**;
- Na aba [Impostos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), o campo **"Cálculo de ICMS, IPI e ISS"** deve estar com a opção **"Não calcula e digita"** selecionada; a marcação **"Tem IPI"** desabilitada; o campo **"Código Sit.Trib.IPI Saída"** com a opção **"(-1) Não sujeita ao IPI"** e a marcação **"Devolver sem destacar IPI"** desativada.
- Na aba [NF-e/NFC-e/CF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abanfe/nfce), o campo **"NF-e"** deve estar selecionado com a opção **"Devolução"**. Caso não queira alterar a TOP, pode informar o CFOP no parâmetro **"CFOP de devolução - CFOPDEVOLUCAO"**. Porém, dessa forma toda nota emitida com esse CFOP vai ter a finalidade de devolução.
- Na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Propriedades](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abapropriedades), a marcação **"Trabalha com IPI ?"** também deve estar realizada.

**Observações:**

- Em qualquer situação que seja diferente da configuração acima, o valor de IPI na Devolução de Compra será informado nos campos próprios e destacados nas tags próprias de IPI, quando a empresa estiver marcada como Trabalha com IPI.
- Se por algum motivo o campo **"C.S.T IPI"** da grade [Itens](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045106793-Central-de-Compras#gradedeitens) na Central de Compras estiver com a opção diferente de **"(-1) Não sujeita ao IPI"**, a tag também não será gerada.
- A nota de devolução deverá ter o destaque do IPI em campos próprios.
- Caso a devolução seja parcial, o valor deverá ser alterado no próprio Portal de Compras. Para isso, acione o botão ![Imagem 1: Caso a devolução seja parcial, o valor deverá ser alterado no próprio Portal de Compras . Para isso, acione o botão…](https://ajuda.sankhya.com.br/hc/article_attachments/16242604375191) **"Devo/Estorn"** e após **"Selecionar Itens"**, informe o valor da devolução na coluna **"Qtd. Faturada"**.
