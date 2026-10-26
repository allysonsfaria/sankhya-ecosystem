---
id: "10928183956375"
titulo: "Impressão de nota fiscal de serviço em contingência"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10928183956375-Impress%C3%A3o-de-nota-fiscal-de-servi%C3%A7o-em-conting%C3%AAncia"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:02:18Z"
rotulos: ["Configuração", "Impressão", "Portal de Vendas", "Contingência", "Prefeituras", "NFS-e", "RPS substitui NFSe temporariamente garantido por impressão", "Cadastre modelo na tela apropriada; modelo é livre", "Marque e imprima RPS converta para NFSe no portal dentro do prazo"]
---

# Impressão de nota fiscal de serviço em contingência

### O que é um Recibo Provisório de Serviços (RPS)

O Recibo Provisório de Serviço (**RPS**) é um documento que tem como função substituir a NFSe temporariamente, e é considerado uma contingência do contribuinte nos casos em que o serviço de NFS-e esteja fora do ar, exista alguma instabilidade na Internet ou qualquer inoperância e é preciso emitir a NFSe.

Então a garantia da veracidade das informações da NFS-e se dará por conta da impressão do RPS.

Importante verificar junto a prefeitura da empresa emitente da NFSe qual é o prazo máximo permitido para conversão do RPS em NFSe, pois através dessa informação será possível prever o tempo máximo que a prefeitura aceita para que esse RPS seja convertido em NFSe.

### Configuração para impressão do RPS

Para emitir uma NFSe em contingência, configure o modelo de impressão na tela Tipos de Operação Top > aba NFS-e > Mod. Imp. RPS.

- **Imp. RPS:** Deve ser previamente cadastrado na tela [Modelos de Nota Fiscal/Duplicatas/Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045109913-Modelos-de-Nota-Fiscal-Duplicatas-Boleto-s-). Este será usado no caso de contingência, quando o serviço de NFS-e estiver fora do ar. O modelo de impressão é livre. Cada empresa terá seu Modelo de impressão de RPS em [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados) ou TXT, de acordo com a legislação de cada município. O sistema usará o modelo de RPS quando a nota for marcada para RPS a pedido do usuário.
- **Observação**: O modelo do RPS deve ser feito considerando o XML do RPS (que o próprio Sankhya gera) ou até mesmo consultas diretas no BD, uma vez que nessa situação não haverá ainda o retorno do XML da aprovação da prefeitura.

![Imagem 1: Observação : O modelo do RPS deve ser feito considerando o XML do RPS (que o próprio Sankhya gera) ou até mesmo…](https://ajuda.sankhya.com.br/hc/article_attachments/19067834038039)

## Fluxo do processo para geração do RPS

### Marcando notas como RPS

No Portal de Vendas selecione a(s) NFS-e(s), acesse o botão NFS-e>>Marcar lote como RPS ou Marcar lote como RPS e imprimir.

**Marcar lote como RPS:** O sistema apresenta a modalidade de contingência eletrônica para notas fiscais eletrônicas de serviço através do **“R.P.S. – "Recibo Provisório de Serviço”**. Constatando-se a impossibilidade do envio de uma **“Nota Fiscal Eletrônica de Serviço”**, deve-se marcá-la através desta opção.

**Marcar Lote como RPS e Confirmar:** Permite confirmar a nota e marcá-la como RPS de uma só vez.

**Marcar lote como RPS e imprimir:** Além de realizar o procedimento descrito na opção anterior, acionando esta opção, será realizada a impressão da nota.

**Observação:** para utilização dessa opção a nota deverá estar Confirmada e com status diferente de Aprovada.

**Desmarcar lote como RPS:** Esta opção pode ser utilizada quando a nota ainda não tiver sido confirmada, e deve ser acionada quando se decide não utilizar a contingência via RPS, por exemplo, quando voltou a internet e é possível transmitir a(s) nota(s), normalmente.

Além das opções já descritas, o usuário também pode utilizar a opção **"Marcar nota como RPS por padrão?"**, localizada na sub-aba Geral -> NFS-e, dentro da aba **"Documentos Fiscais Eletrônicos"** nas preferências da empresa. Quando ativada, todas as notas de serviço geradas serão automaticamente marcadas como RPS.

### Convertendo um RPS em uma NFSe

Para enviar um RPS à prefeitura e convertê-lo em uma NFSe, acesse o Portal de Vendas, selecione a nota e, na opção “NFSe”, clique em “Gerar Lote”

**Gerar Lote:** Efetua o envio do RPS ao serviço de NFS-e da prefeitura (webservice).

**Buscar autorização:** Utilizado nos casos em que após o envio do lote, o status de processamento do RPS retorna como **"Aguardando Autorização"**.

**Importante:** Após a impressão do RPS, sua conversão em NFS-e fica sob responsabilidade do usuário, que deve efetuar o envio do RPS ao serviço de autorização da prefeitura dentro do prazo estabelecido na legislação municipal, sob pena de multa estabelecida pelo município, se atente a essas regras.

### Informações Importantes sobre o Processo:

Só será possível desmarcar uma nota como RPS através da opção **"Desmarcar Lote como RPS"** se o boleto não tiver sido gerado e nem a nota/boleto enviados por e-mail.

O usuário poderá imprimir manualmente a nota e o boleto deste RPS e enviar ambos por e-mail.

Se configurado para o envio automático de e-mails, o sistema enviará o boleto e a nota automaticamente, mesmo que já tenham sido enviados manualmente, assim que a nota marcada como RPS for aprovada.
