---
id: "44010625923095"
titulo: "[TMS] - Cadastro de Campanhas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010625923095--TMS-Cadastro-de-Campanhas"
trilha: "Lincros > TMS > Campanhas - TMS"
atualizado_em: "2026-10-05T18:42:37Z"
rotulos: ["sync_hc", "lincros", "lincros_13432744", "sync_hash_1b04a8882467"]
---

# [TMS] - Cadastro de Campanhas

**Menu**: Cadastros gerais > Campanhas

**Objetivo:** Como realizar o cadastro de campanhas

## Considerações:

- A função campanha destina-se às empresas que desejam criar promoções de frete para seus clientes;
- Sempre que um cliente fizer uma consulta de frete no seu site, o sistema verifica se existe uma campanha disponível que se enquadre no pedido, e retorna o valor do frete com base no estabelecido na campanha;
- Esta funcionalidade permite a combinação de um formato de frete a um ou mais critérios válidos para uma campanha;
- Importante ressaltar que a campanha é uma funcionalidade voltada à informação do custo de frete ao cliente final, ou seja, ela não altera o custo de frete para o embarcador;
- Foi desenvolvido um parâmetro para habilitar a campanha no Webservice chamado 'orfertarCampanhaFrete';

Abaixo segue os procedimentos:

1. Clicar na opção 'Novo';
2. Preencher os campos conforme abaixo:

- **Código:** Preencher com um código que pode conter letras e números. O TMS envia no WS de /cálculo para informar à qual campanha aquela transportadora se encaixou.
- **Descrição:** Definir o título da campanha
- **Unidade:** Este campo define a unidade da campanha. A campanha é válida por unidade, sendo necessário duplicá-la caso se aplique a mais unidades.
- **Ativo:** Este campo define se a campanha está ativa ou não
- **Aplicável apenas para a tabela de fretes de menor valor:** Define o critério de tabela de menor valor será utilizado.
- **Formato de Prazo:** Define os dias a mais no prazo de entrega. É possível acrescentar dias ao prazo original de entrega sem a necessidade de alterar as tabelas de prazo.
- **Formato de cálculo:** Define qual será o formato de cálculo utilizado:

  - **Desconto valor fixo:** informar o valor fixo de desconto que será aplicado ao frete
  - **Desconto percentual:** informar o valor percentual de desconto que será aplicado ao frete
  - **Valor máximo:** Definir o valor máximo que um frete pode custar.
  - **Valor fixo:** informar o valor fixo de frete que o cliente irá pagar.
  - **Frete grátis:** Define o frete como gratuito ao cliente.

![Imagem 1: Frete grátis: Define o frete como gratuito ao cliente.](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963112372/c2992a281c2356fd49e42f62c269/00A4BCC5053C8B9905601F0090BED4A9?expires=1791331200&signature=5dc3e85f13d15ae4d5931e30c3e40679ba77810029d8fa7d79030d5d6449f5c2&req=dSkhFch%2Fn4JYW%2FMW3nq%2Bgc8pmQUft2i6dHlsE%2BoLqIA1NEk04cwJ1pAmZhOQ%0ALgPe4zvFKB0YZPWh%2FX1Hok89Qjw%3D%0A)

3. Definido o formato de cálculo, é possível definir os critérios utilizados para a aplicação da campanha.

**Importante:** Se não for definido um critério, o sistema entende que a campanha abrange o todo. Se for definido um critério, o sistema restringe a campanha somente àquele critério. Quanto mais critérios definidos, mais restrita é a campanha.

![Imagem 2: Importante: Se não for definido um critério, o sistema entende que a campanha abrange o todo. Se for definido um…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963112402/b732bb7ea89fb0a329d9eaf9ef9e/7E7D5A43CCAA122FDE84705F406C185D?expires=1791331200&signature=cfd20fe5726bc6c65b3456c313288de948e28619bbad6c084fed5946cedd9104&req=dSkhFch%2Fn4VfW%2FMW3nq%2Bgd6DSrFUh24f8EinAU5ub2TURrwKrgZkHgyT777M%0AfXR6OierochPWeORa886xy8ERMk%3D%0A)

- **Vigência:** Definir o início e o fim da vigência da campanha. É possível selecionar dias da semana específicos para que ela esteja ativa.

  ![Imagem 3: Vigência: Definir o início e o fim da vigência da campanha. É possível selecionar dias da semana específicos para que…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963112417/07be3fb68ac473a24a53d22809be/B6384A02F2B2741306ECC7D278DC3073?expires=1791331200&signature=108bd2f7154b90a155ef515e483692e4bc3d564b78549c08d83d04ead629dfbd&req=dSkhFch%2Fn4VeXvMW3nq%2BgbQd3Etry5l7aHh7hdNv%2BsxSFdNGQYu7yC8Yyg0Z%0AJYslvSrDIIOQ97aCg3cO6u5sHFc%3D%0A)
- **Cliente:** Definir os clientes aos quais a campanha é destinada

  ![Imagem 4: Cliente: Definir os clientes aos quais a campanha é destinada](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963112429/770584fc02c462b50d4ff8decc08/6E36D01496BBFA40BE77F3E5F08378AA?expires=1791331200&signature=f78e4c07a1304feb36075fb23da7a8101fe97e1de761bfa0d6e24adfd71ffb24&req=dSkhFch%2Fn4VdUPMW3nq%2BgaZUiTL2OEaoB%2FqF5flMPU7tGWa86esEbofEeHdz%0AJcqeA8lhhA4y4r1qGcQUozRgxyA%3D%0A)
- **Localidade:** Define para quais localizações a campanha será aplicada, podendo ser faixas de CEP, regiões, cidades ou estados.

  ![Imagem 5: Localidade: Define para quais localizações a campanha será aplicada, podendo ser faixas de CEP, regiões, cidades ou…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963112464/6277098c3bcf3fe43cd3364787df/B7D62776A5F6E8C7546FE1E220836CD5?expires=1791331200&signature=07c39a6fd896caee9bb860dc201279166e2993be42f2c2642f5c6bc7d7008622&req=dSkhFch%2Fn4VZXfMW3nq%2BgTT6m0KHSIgyvqNLwYt4ou79DWa0gVxemBsAT7Dq%0AvBAWtuauCNAw2Hn6agpS0xxYwiw%3D%0A)
- **Valor:** Definir o valor do pedido ao qual a campanha será aplicada; **Acima de**: Campanha é aplicada em pedidos cujo valor ultrapasse o definido; **Até**: Campanha é aplicada em pedidos cujo valor não ultrapasse o definido.

  ![Imagem 6: Valor: Definir o valor do pedido ao qual a campanha será aplicada; Acima de : Campanha é aplicada em pedidos cujo valor…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963112481/954cdefb9f172e28aafac82b1304/A059A58EC4AB56E1BB529A8314FBD7D2?expires=1791331200&signature=80ef483485223c4254f5331cc994b95c86a324d4274bd150e67dfa005e3dbb94&req=dSkhFch%2Fn4VXWPMW3nq%2BgbRPoy2GlyZcWuyJCmmhyG%2FxCoKIV5LOQPPzftuY%0AZL%2FDdSPEaoXzRm85yfLtzkdvvFE%3D%0A)
- **Marcador**: Havendo necessidade de restringir campanhas, um Marcador poderá ser vinculado. Com isto, a campanha será somente retornada no cálculo, caso este marcador tenha sido enviado na requisição.

  ![Imagem 7: Marcador : Havendo necessidade de restringir campanhas, um Marcador poderá ser vinculado. Com isto, a campanha será…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963112496/b27f5f459badecd300a3ac3e29e1/F0C2FC7C7C5BE43602F065DF5F1E0CAF?expires=1791331200&signature=e61227695cc561973383630521283bbb5bf5fc97633e856d5c4ba8a18bdfff2b&req=dSkhFch%2Fn4VWX%2FMW3nq%2BgTxDwgZ0NafmCC8opCtymaoGqoHuHuWcmykptOjY%0AL3GBE7SG2MZ5%2Bd%2FtueVGYuWxcnY%3D%0A)
- **Tabelas de frete:** Define as tabelas de frete que serão utilizadas na campanha.

  ![Imagem 8: Tabelas de frete: Define as tabelas de frete que serão utilizadas na campanha.](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963112513/e8c46c51e124f9342b8519b3146d/5F908F0F0C16E7AF9492AEBC722312FF?expires=1791331200&signature=485f9e83c18580ba5f307e6159ccba3e0a68057c0d9271eea1988750779297fe&req=dSkhFch%2Fn4ReWvMW3nq%2BgXgUZFgnUbDPOx7JsR8xTtTq40gwXfAWrpcXhKe%2B%0AT85qs0ZCLfkphoTxsNmWrDqk2nM%3D%0A)

Você pode também extrair um relatório sobre as campanhas [clicando aqui](https://sankhya.zendesk.com/hc/pt-br/articles/44010625923095).

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
