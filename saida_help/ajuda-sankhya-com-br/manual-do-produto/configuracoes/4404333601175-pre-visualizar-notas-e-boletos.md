---
id: "4404333601175"
titulo: "Pré-visualizar notas e boletos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4404333601175-Pr%C3%A9-visualizar-notas-e-boletos"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-10-08T12:39:46Z"
rotulos: ["Configuração", "Portal de Compras", "Relatórios Formatados", "Relatórios", "NF-e", "Portal de Vendas", "XML", "Boletos", "Preferências", "botão pré-visualizar", "Configuração de Pré-Visualização: Notas e Boletos", "Documentos Eletrônicos"]
---

# Pré-visualizar notas e boletos

É possível configurar para utilizar o visualizador nativo do sistema operacional na pré-visualização de notas de compra e venda e boletos.

Para configurar a opção de Pré-Visualizar Nota de Compra e Venda, realize as seguintes configurações:

1. Desabilite o parâmetro **"Utilizar JasperViwer p/ visualização de relatório? - UTZJASPERWC"**;
2. Configure um modelo no campo **"Relatório formatado do DANFE"** das [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Documentos fiscais eletrônicos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abaDocumentosFiscaisEletr%C3%B4nicos), sub-aba [NF-e/NFC-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#Sub-abaNF-e/NFC-e) > [NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#sub-abaNF-e); este modelo é utilizado tanto para impressão do DANFE quanto para pré-visualizar a nota.
3. Com o número do relatório, localize o arquivo .jrxml e adicione nos arquivos a propriedade **<property name="forceDownloadElectron" value="true"/>** junto às demais.

Assim, ao acessar os Portais de Compra e Venda e clicar no botão **"Pré-visualizar"**, opção **"Pré-Visualizar Nota"**, o sistema irá utilizar o visualizador de PDF padrão do sistema operacional.

**Observação:** o mesmo ocorre quando é utilizado o navegador Google Chrome.

Agora, para configurar a opção de Pré-Visualizar Boletos, faça as configurações abaixo:

1. Desabilite o parâmetro de chave UTZJASPERWC;
2. Acesse a tela [Modelos de Boleto(s)](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607134-Modelos-de-Boleto-s-) e localize o boleto desejado;
3. No arquivo .jrxml adicione a propriedade **'<property name="forceDownloadElectron" value="true"/>'** junto às demais.

Após essa alteração, o sistema irá utilizar o visualizador nativo do sistema operacional para pré-visualizar os boletos, sendo que o mesmo comportamento ocorre quando for utilizado o navegador Google Chrome.

Por fim, para configurar a Visualização de Relatórios Formatados, realize as configurações seguintes:

1. Desabilite o parâmetro de chave UTZJASPERWC;
2. Acesse a tela [Relatórios Formatados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597694-Relat%C3%B3rios-Formatados);
3. Nos arquivos .jrxml adicione a propriedade **'<property name="forceDownloadElectron" value="true"/>'** junto às demais propriedades.

**Observação:** com o parâmetro **"Forçar o download de relatórios internos? - FORCEDOWNLOAD"** ligado e o parâmetro UTZJASPERWC desligado, quando você efetuar o download do relatório interno, ele será apresentado no visualizador nativo do sistema.
