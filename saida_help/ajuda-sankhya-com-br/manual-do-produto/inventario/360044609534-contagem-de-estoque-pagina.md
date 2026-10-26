---
id: "360044609534"
titulo: "Contagem de Estoque (Página)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609534-Contagem-de-Estoque-P%C3%A1gina"
trilha: "Manual do Produto > Suprimentos e Estoque > Inventário"
atualizado_em: "2026-07-29T14:48:46Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Impressão", "Relatórios", "Inventário", "WMS", "Contagem de Estoque (Página)", "br.com.sankhya.contagem.estoque.pagina", "Contagem de Estoque (Página) manual", "IReport", "Estoque", "Cópia de Estoque", "Lançar contagem página", "Emitir relatório estoque", "Salvar contagem atual"]
---

# Contagem de Estoque (Página)

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42312595726231) Módulo: Inventário > Avançado
```

---

O primeiro passo para proceder com a contagem por página, é elaborar um relatório da Cópia do Estoque. Esse relatório deve ser elaborado com o iReport 4 ou superior, e cadastrado no sistema pela tela [Cópia de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609654-C%C3%B3pia-de-Estoque). É imprescindível que o relatório seja cadastrado e emitido através dessa tela. O relatório deve ter como base, a view VGFCTE incluir os campos VGFCTE.CODPROD, VGFCTE.CODLOCAL e VGFCTE.CONTROLE para que as linhas com as páginas sejam incluídas corretamente.

| [Funcionalidades da tela](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609534-Contagem-de-Estoque-P%C3%A1gina#funcionalidadesdatela) |  | [Incluindo Relatório no iReport](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609534-Contagem-de-Estoque-P%C3%A1gina#incluindorelat%C3%B3rionoireport) |
| --- | --- | --- |

                                                  

![Imagem 2: Incluindo Relatório no iReport](https://ajuda.sankhya.com.br/hc/article_attachments/360086864594)

Ao emitir o relatório, é exibido o diálogo para informar os parâmetros do relatório e a opção se a numeração será gerada ou não. Para maiores detalhes consulte o tópico abaixo [Incluindo Relatório no iReport](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609534-Contagem-de-Estoque-P%C3%A1gina#incluindorelat%C3%B3rionoireport).

Após emitir o relatório, e a Contagem do Estoque for efetuada, essa contagem deve ser lançada na tela Contagem de Estoque (Página). Nessa tela, você pode pesquisar as impressões lançadas pelo sistema. Ao selecionar uma impressão, o sistema traz os produtos inseridos pelo relatório, e assim, você poderá navegar entre as páginas. Ao posicionar em uma página de uma impressão, você poderá então, editar as quantidades de cada linha.

Após lançar as quantidades, clique no botão **"Salvar"**, para que a contagem seja incluída. Ao clicar nesse botão, o sistema apresenta uma última tela, perguntando a empresa e a data para a qual será lançada a contagem. Caso haja uma contagem em andamento para aquela data, o sistema te questiona se deve-se atualizar a contagem atual ou lançar uma nova contagem. Clicando em **"OK"**, a contagem é salva/incluída.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609534-Contagem-de-Estoque-P%C3%A1gina#top)

## Funcionalidades da tela

Através do botão  **"Configurar Grade"**, você poderá selecionar os campos que aparecerão na grade.

No campo **"Nro Impressão"**, informe o número da impressão que foi gerado no relatório de Cópia do Estoque. Ao lado do campo, tem o botão de Pesquisa que trará todos os números de impressões já efetuados.

O botão ![Imagem 3: O botão ficará habilitado, se houver uma página anterior à informada no campo "Página" .](https://ajuda.sankhya.com.br/hc/article_attachments/360084383533) ficará habilitado, se houver uma página anterior à informada no campo **"Página"**.

Informe no campo Página, a página do relatório que foi gerado para informar a quantidade dos produtos que foi efetuada a contagem.

O botão ![Imagem 4: O botão ficará habilitado, se houver uma página posterior à informada no campo Página .](https://ajuda.sankhya.com.br/hc/article_attachments/360083212054) ficará habilitado, se houver uma página posterior à informada no campo Página.

O botão **"Aplicar"** verificará se o número da impressão e da página forem informados, se sim, trará os produtos em conformidade ao relatório gerado na Cópia de Estoque. Caso os campos não forem informados, o sistema emitirá uma mensagem solicitando o preenchimento.

Clicando em **"Salvar"**, você salvará a contagem efetuada dos produtos na grade da página configurada.

O botão **"Cancelar"**, se acionado, cancelará a operação efetuada.

Na grade, somente o campo **"Quantidade"** poderá ser alterado e informado, os outros campos aparecerão desabilitados.

Após lançar as quantidades, clique no botão Salvar, para que a contagem seja incluída. Ao clicar nesse botão, o sistema apresenta uma última tela, perguntando a empresa e a data para a qual será lançada a contagem. Caso haja uma contagem em andamento para aquela data, o sistema te questiona se ele deve atualizar a contagem atual ou lançar uma nova contagem.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609534-Contagem-de-Estoque-P%C3%A1gina#top)

## Incluindo Relatório no iReport

Para que seja possível utilizar a Contagem de Estoque (Página), é necessário, inicialmente, configurar um Relatório através do iReport. Este se encontra disponível no site de [downloads.sankhya.com.br](http://downloads.sankhya.com.br/) para instalação.

A consulta do relatório fica a seu critério, mas existem quatro campos que são obrigatórios para que seja possível a geração do relatório, são eles:

- CODPROD;
- CODVOL;
- CONTROLE;
- CODLOCAL.

Estes campos advirão da view **VGFCTE**.

Além disso, deverá realizar a criação do parâmetro **NUMERO\_IMPRESSAO**. Este parâmetro servirá para indicar, no momento da geração do relatório de cópia, qual é o número gerado para ser utilizado posteriormente na Contagem de Estoque por página:
![Imagem 5: Além disso, deverá realizar a criação do parâmetro NUMERO_IMPRESSAO . Este parâmetro servirá para indicar, no momento…](https://ajuda.sankhya.com.br/hc/article_attachments/16251878588183) No Ireport, no painel Parameters: Adicione o Parameter e informe o nome do Parâmetro para NUMERO\_IMPRESSAO;
![Imagem 6: Além disso, deverá realizar a criação do parâmetro NUMERO_IMPRESSAO . Este parâmetro servirá para indicar, no momento…](https://ajuda.sankhya.com.br/hc/article_attachments/16251836514967) Após a criação do parâmetro, coloque-o no Designer, desmarcando a opção "Use as a prompt" das Propriedades do Parâmetro dentro do Ireport.
Efetue as configurações do layout caso necessário, e salve o relatório.
**Observação:** será necessário efetuar a cópia do estoque antes, para ser possível visualizar o relatório.

Após a criação do relatório, você deve configurar no Sankhya Om, a Geração da Cópia do Estoque em [Cópia de Estoque](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609514); pois, para efetuar a contagem, é necessário efetuar a cópia do estoque antes.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044609534-Contagem-de-Estoque-P%C3%A1gina#top)
