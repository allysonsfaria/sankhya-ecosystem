---
id: "360045115493"
titulo: "Recuperação de Devedores Duvidosos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045115493-Recupera%C3%A7%C3%A3o-de-Devedores-Duvidosos"
trilha: "Manual do Produto > Fiscal e Contábil > Contábil > Contabilização"
atualizado_em: "2026-07-29T16:01:30Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "Movimentação Financeira", "Perda", "Gerência de Cobrança", "PDD", "Recuperação de Devedores Duvidosos", "br.com.sankhya.recuperacao.devedores.duvidosos", "Recuperação de Devedores Duvidosos manual", "Crédito", "Contabilização", "Financeiro", "Cálculo de Juros e Multas", "Renegociação e centro de resultado", "Provisão e recuperação de créditos", "Opções de exportação e visualização"]
---

# Recuperação de Devedores Duvidosos

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42314931976087)Módulo: Contabilização > Arquivos
```

---

Em diversas atividades empresariais, é comum a empresa ter títulos de clientes que já estão vencidos a algum tempo. Estes títulos podem constituir **"Perdas no Recebimento de Créditos"**, esta é a caracterização da **"Provisão de Devedores Duvidosos" (PDD)**.

Quando um título já considerado incobrável é recebido, ocorre a chamada **"Recuperação do Crédito"**. Neste caso, deve-se dar entrada do valor no caixa da empresa e considerar essa recuperação de crédito.

A marcação **"Considerar títulos renegociados"** tem o objetivo de apresentar na tela, os títulos renegociados que foram contabilizados como PDD, para que seja possível realizar a recuperação dos mesmos para a compensação dos lançamentos dos títulos originais. 

Quando a marcação estiver habilitada, o sistema irá apresentar na tela os lançamentos do tipo **"RECDESP = 0"**, alterados a partir da rotina de renegociação. Se não estiver marcada, não serão apresentados os títulos renegociados.

A grade desta tela mostrará os títulos filtrados e na parte lateral os botões para controle da grade e do resultado.

![Imagem 2: A grade desta tela mostrará os títulos filtrados e na parte lateral os botões para controle da grade e do resultado.](https://ajuda.sankhya.com.br/hc/article_attachments/7175387029527)

No Painel de Filtros temos a marcação **"Usar Centro de Resultado?"**, que ao habilitá-la, o sistema buscará o Centro de Resultado informado no campo **"Centro de Resultado"** da aba [Lançamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601874#abalanamento) da [Movimentação Financeira](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114753-Movimenta%C3%A7%C3%A3o-Financeira). Porém, se esse campo não estiver preenchido, o sistema irá considerar o valor **"0"** para a contabilização. 

Além disso, se a marcação **"Centro de Resultado obrigatório"** do [Plano de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608054-Plano-de-Contas) utilizado estiver selecionada, a marcação Usar Centro de Resultado, também deve ser habilitada.

**Observação:** a marcação Usar Centro de Resultado? será apresentada na tela Recuperação de Devedores Duvidosos, quando a marcação **"Utiliza centro de resultado"** da aba [Lançamentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa#abalanamentos) da tela [Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa) (Contabilidade > Preferências) estiver ligada.

Serão listados apenas os títulos contabilizados e que tenham a marcação **"PDD"** igual a **"Sim"**, ou seja, é possível recuperar os devedores duvidosos, ou seja, um título marcado como PDD e contabilizado, é possível recuperá-lo contabilizando novamente em outra conta débito e crédito e alterando o campo PDD do título financeiro para 'Não'.

Na parte inferior da grade são apresentados os totalizadores mostrando a quantidade de títulos e o valor total dos mesmos.

A documentação dos campos desta tela é idêntica à da tela [Contabilização de Devedores Duvidosos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607634).

No alto da tela, tem-se o botão ![Imagem 3: No alto da tela, tem-se o botão "Impressão do Grid" , onde define-se como será realizada a visualização dos resultados…](https://ajuda.sankhya.com.br/hc/article_attachments/16541930731159) **"Impressão do Grid"**, onde define-se como será realizada a visualização dos resultados da tela; pode-se utilizar as seguintes opções:

**Lupa (Impressão do Grid):** Selecionando-se esta opção será aberta uma tela de visualizador de arquivos com as informações da tela.

**Exportar como PDF:** Por esta opção, tem-se as informações no formato PDF.

**Exportar como planilha:** Através desta opção, os dados serão baixados automaticamente no formato XLS.

**Visualizar em cubo...:** Por esta alternativa, será aberta uma tela referente ao visualizador de arquivos contendo as informações em cubo.

**![Imagem 4: Informações Adicionais](https://ajuda.sankhya.com.br/hc/article_attachments/26161522516503) Informações Adicionais**

**(1)** O parâmetro **"Apresentar tít. de PDD assumindo o Vlr. de Lanç - TITPDDVLRLANC"** serve para definir a utilização do valor a ser validado para apresentação dos títulos contabilizados como PDD na tela de Recuperação de Devedores Duvidosos. 

Sendo assim, se o parâmetro estiver ligado e os títulos tenham sido contabilizados como Devedores Duvidosos, seja pela rotina [Contabilização Devedores Duvidosos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607634-Contabiliza%C3%A7%C3%A3o-de-Devedores-Duvidosos) ou [Agendamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608294-Agendamento), quando for acionada a rotina de Recuperação de Devedores Duvidosos, o sistema irá apresentar os títulos contabilizados anteriormente, assumindo assim o valor do Lançamento Contábil. Utilizando o parâmetro desligado, o comportamento anterior do sistema se mantém, apresentando então o Valor do Desdobramento do título do financeiro.

**(1)** Em casos de baixas parciais, o sistema gera um novo título para o valor remanescente, porém esse novo título perde o vínculo com o original, exigindo que seja contabilizado novamente como PDD para permitir sua recuperação no momento da baixa.

Para garantir que a contabilização ocorra corretamente e evitar duplicidade de valores, ative o parâmetro TITPDDVLRLANC. Este parâmetro utiliza o valor do lançamento contábil original do PDD, permitindo que a recuperação seja baseada no valor original do título, e não apenas na baixa parcial.

Dessa forma, os novos títulos gerados como pendentes seguem o fluxo normal, isto é, eles devem ser marcados como PDD para aparecerem na tela de Contabilização de Devedores Duvidosos e, após a contabilização, estarão disponíveis na tela de Recuperação de Devedores Duvidosos para a devida recuperação.
