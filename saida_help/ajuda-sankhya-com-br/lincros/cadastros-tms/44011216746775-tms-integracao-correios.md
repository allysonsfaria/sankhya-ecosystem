---
id: "44011216746775"
titulo: "[TMS] - Integração Correios"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44011216746775--TMS-Integra%C3%A7%C3%A3o-Correios"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T18:59:41Z"
rotulos: ["sync_hc", "lincros", "lincros_13438900", "sync_hash_9fec4ff1e90b"]
---

# [TMS] - Integração Correios

**Menu**: Cadastros Gerais > Transportadoras > Correios > Configurações

**Objetivo**: Com essa integração, será possível buscar de forma automática os valores de Preço, Prazo e Ocorrências dos correios sem a necessidade de cadastros manuais de tabela de frete e atualização de valores. Ainda, será possível obter os valores dos diferentes serviços prestados (Sedex, Sedex10, PAC, e etc.).

**Considerações**: Permitir que sejam cadastrados parâmetros específicos para cada um dos serviços abaixo:

- Busca de preço e prazo;
- Busca de ocorrências;

Para ativar a integração com o Correios basta seguir os procedimentos abaixo:

1. Acessar o menu: Cadastros Gerais > Transportadoras > Correios > Configurações;
2. Inserir as informações abaixo que foram recebidos do serviço do Correios;

   ![Imagem 1: Inserir as informações abaixo que foram recebidos do serviço do Correios;](https://ajuda.sankhya.com.br/hc/article_attachments/44011247981207)
3. Deve ser marcado o checkbox  'Integrar com os Correios' para que a integração com estes serviços seja ativada;
4. Para 'Cálculo de preço e prazo' inserir as informações:

No campo 'Código de empresa': Informar o código Administrativo Correios (8 dígitos);
No campo 'Senha': Informar a senha (8 dígitos) do padrão dos correios e definir como os 8 primeiros dígitos do CNPJ do contrato;

![Imagem 2: No campo 'Código de empresa': Informar o código Administrativo Correios (8 dígitos); No campo 'Senha': Informar a senha…](https://ajuda.sankhya.com.br/hc/article_attachments/44011265286039)

5. Para “Integração de ocorrências” inserir as informações:

No campo Usuário: Informar o código do contrato recebido pelo correios SRO (normalmente possui 10 dígitos);

No campo Senha: Informar a senha do contrato SRO;

6. Deve ser realizado o cadastro da tabela de fretes pelo menu: Cadastros Gerais> Transportadoras > Negociações >Tabelas de frete;

**Importante**: Uma tabela de frete deve ser cadastrada com a transportadora 'ECT EMP BRAS DE CORREIOS E TELEGRAFOS' e com uma rota que seja 'Brasil x Brasi'l e faixa de peso de "0" ao infinito.

Mas esta não é uma regra, o cliente pode aplicar 'Filtros' por meio de rotas mais específicas para que, por exemplo, o TMS refine quais rotas poderão ofertar fretes pelo Correios.

![Imagem 3: Mas esta não é uma regra, o cliente pode aplicar 'Filtros' por meio de rotas mais específicas para que, por exemplo, o…](https://ajuda.sankhya.com.br/hc/article_attachments/44011280114071)

A tabela de frete do Correios possui as mesmas premissas de uma tabela normal, sendo assim pode ser utilizado os parâmetros padrões de uma tabela, como:

- Restrições
- Marcadores
- Vigência
- Tipo de negociação
- Unidades

7. No modal da tabela de frete é necessário informar o serviço do Correios (PAC, Sedex, etc);

![Imagem 4: 7. No modal da tabela de frete é necessário informar o serviço do Correios (PAC, Sedex, etc);](https://ajuda.sankhya.com.br/hc/article_attachments/44011217403159)

8. É necessário criar uma tabela com cada modal, caso o cliente utilize mais opções de serviço do Correios;

9. Caso o modal não esteja disponível na aba "Cadastro" da tabela de fretes, adicionar o modal na aba "Restrições de busca" como atendido;

10. Após adicionar e salvar, retornar a aba cadastro e verificar se o modal foi atualizado;

![Imagem 5: 10. Após adicionar e salvar, retornar a aba cadastro e verificar se o modal foi atualizado;](https://ajuda.sankhya.com.br/hc/article_attachments/44011248672919)

## Premissas para cálculo de preço e prazo:

- Informação de login e senha cadastrados;
- Ativação da integração habilitada;
- Tabela de fretes por serviço Correios (PAC, Sedex e etc.);
- Rota Brasil x Brasil ou detalhada;
- Componente em generalidades (Valor Correios);
- Deferimento de tabela;
- Adicionar restrição com o modal atendido;

## Componente valor correios:

![Imagem 6: Componente valor correios:](https://ajuda.sankhya.com.br/hc/article_attachments/44011280454295)

A integração após finalização do cadastro, leva cerca de 02 horas para ser ativada, e pode ser testada pela calculadora de fretes.

## Prazo

O Lincros pode buscar o prazo com base em uma tabela de prazo padrão para Correios, cadastrada manualmente ou buscar automaticamente pelo webservice, para esta segunda opção solicitar ao suporte a habilitação do serviço (gratuito).

Parâmetro a ser ativado: buscarPrazoEntregaCorreios = true

## Ocorrências

Para buscar as ocorrências dos Correios é necessário receber no Lincros o código do objeto, podemos receber o código das seguintes formas:

- Via importação de planilha

No menu Entregas e Ocorrências > Acompanhamento de Entregas, você pode baixar a planilha modelo de código de correios e fazer o preenchimento manualmente:

![Imagem 7: No menu Entregas e Ocorrências > Acompanhamento de Entregas, você pode baixar a planilha modelo de código de correios e…](https://ajuda.sankhya.com.br/hc/article_attachments/44011248970135)

Após o preenchimento da planilha, você deve pressionar o mesmo botão, sem pressionar na flecha que habilita o submenu de modelo para fazer o upload.

![Imagem 8: Após o preenchimento da planilha, você deve pressionar o mesmo botão, sem pressionar na flecha que habilita o submenu…](https://ajuda.sankhya.com.br/hc/article_attachments/44011280651159)

Os pré-conhecimentos vinculados a NF serão populados a informação com o código do objeto:

![Imagem 9: Os pré-conhecimentos vinculados a NF serão populados a informação com o código do objeto:](https://ajuda.sankhya.com.br/hc/article_attachments/44011249256599)

O Lincros irá buscar no web service dos correios, as ocorrências vinculadas a estes objetos de uma em uma hora, atualizando na régua de acompanhamento de entregas:

![Imagem 10: O Lincros irá buscar no web service dos correios, as ocorrências vinculadas a estes objetos de uma em uma hora,…](https://ajuda.sankhya.com.br/hc/article_attachments/44011234119575)

**Obs**: É importante fazer o de/para das ocorrências dos correios, pois eles utilizam um padrão próprio, diferente do padrão PROCEDA através do menu: Cadastros Gerais>Transportadoras>Ocorrências>Transportadora.

Além da planilha pode ser importado os códigos dos correios por:

- ## Via configuração TF

No XML da nota fiscal inserido uma nova chave para que seja informado o código do objeto. O campo deve estar na chave de INF ADICIONAL:

![Imagem 11: No XML da nota fiscal inserido uma nova chave para que seja informado o código do objeto. O campo deve estar na chave…](https://ajuda.sankhya.com.br/hc/article_attachments/44011234229911)

- ## Via Webservice

É enviado via integração para o Lincros o código do objeto vinculado ao documento já importado.

Se a integração estiver ativa e possuirmos o código do objeto, o Lincros irá buscar automaticamente as ocorrências de entrega do Correios. Para este caso, buscar a documentação com o suporte.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
