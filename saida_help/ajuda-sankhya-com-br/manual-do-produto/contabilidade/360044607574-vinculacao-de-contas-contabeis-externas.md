---
id: "360044607574"
titulo: "Vinculação de Contas Contábeis Externas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607574-Vincula%C3%A7%C3%A3o-de-Contas-Cont%C3%A1beis-Externas"
trilha: "Manual do Produto > Fiscal e Contábil > Contábil > Contabilidade"
atualizado_em: "2026-07-29T16:01:50Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "ECD", "Contas", "Externas", "Vinculação", "br.com.sankhya.mgecontab.vinculocontascontabeis", "Vinculação de Contas Contábeis Externas manual", "Contas Contábeis", "Contabilidade", "Contábeis", "Plano de Contas", "Vinculação de Contas: Integração entre Filiais e Matriz"]
---

# Vinculação de Contas Contábeis Externas

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42314969412375) Módulo: Contabilidade> Arquivos
```

---

Por meio dessa tela você irá criar um mapeamento de contas externas de Filiais, relacionando-as com as contas padrão da Matriz. Essa rotina deverá ser utilizada por empresas filiais que utilizam um Plano de Contas diferente do cadastrado no sistema, de modo que, para filiais que possuem o mesmo Plano de Contas, não se faz necessária sua importação.

| [Preenchimentos Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607574-Vincula%C3%A7%C3%A3o-de-Contas-Cont%C3%A1beis-Externas#preenchimentosiniciais) | [Aba Vinculação de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607574-Vincula%C3%A7%C3%A3o-de-Contas-Cont%C3%A1beis-Externas#abavinculaodecontas) |
| --- | --- |
| [Sub-aba Geral](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607574-Vincula%C3%A7%C3%A3o-de-Contas-Cont%C3%A1beis-Externas#h_af5fa024-92af-4c92-a799-e5179dad31d2) | [Aba Máscara Conta Externa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607574-Vincula%C3%A7%C3%A3o-de-Contas-Cont%C3%A1beis-Externas#abamscaracontaexterna) |

                                                           

![Imagem 2: Aba Máscara Conta Externa](https://ajuda.sankhya.com.br/hc/article_attachments/360073007194)

## Preenchimentos Iniciais

Primeiramente nesta tela, preencha o **"Cód. Empresa da Importação"**, ou seja, o código da empresa da qual serão realizados os vínculos das contas externas às contas contábeis da empresa detentora do Plano de Contas.

Informe uma **"Descrição"** adequada ao vínculo, com um tamanho máximo de 40 (quarenta) caracteres.

Ao acionar a marcação **"Gerar no I157 da ECD"**, as contas vinculadas serão geradas no registro I157 (layout 8) da ECD.

Por meio do campo **"Data Início da Mudança do Plano de Contas"**, indique em qual data se iniciou a mudança do plano de contas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607574-Vincula%C3%A7%C3%A3o-de-Contas-Cont%C3%A1beis-Externas#top)

## Aba Vinculação de Contas

![Imagem 3: Aba Vinculação de Contas](https://ajuda.sankhya.com.br/hc/article_attachments/360080581854)

Informe inicialmente nesta aba, a **"Conta Reduzida"**, onde serão disponibilizadas para escolha somente contas ativas e analíticas pertencentes a Empresa dona do Plano de Contas.

Ao salvar o registro, automaticamente o sistema irá buscar o Plano de Contas da empresa selecionada, e disponibilizará seu plano de contas para que se possa realizar o vínculo com as Contas Contábeis Externas.

Vincule a mesma Conta contábil resumida a várias Contas Contábeis Externas. Deve-se para isso, informe a Conta Reduzida e os códigos das contas externas; o sistema organizará a ordem das contas contábeis repetidas através do campo **"Sequência"**.

Por meio do botão ![Imagem 4: Por meio do botão "Atualizar contas" presente no alto da aba, tem-se a verificação da existência de novas contas para a…](https://ajuda.sankhya.com.br/hc/article_attachments/5316318806551) **"Atualizar contas"** presente no alto da aba, tem-se a verificação da existência de novas contas para a empresa do plano de contas do vínculo selecionado, em caso positivo, as novas contas serão inseridas na tabela.

A exclusão será feita automaticamente, ou seja, se a conta for excluída (Plano de Contas) o registro nesta aba também será excluído.

Por meio do campo **"Centro de Resultado"** você poderá vincular o CR na Conta Contábil para alimentar o registro I157 da ECD.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607574-Vincula%C3%A7%C3%A3o-de-Contas-Cont%C3%A1beis-Externas#top)

## Sub-aba Geral

![Imagem 5: Sub-aba Geral](https://ajuda.sankhya.com.br/hc/article_attachments/29119747313431)

Referente ao campo **"Conta contábil externa importada"**, pode-se realizar o vínculo de uma conta contábil. Para isso, clique no campo de pesquisa à frente do campo e escolha a Conta importada na rotina de Importação do Plano de Contas. Serão apresentadas apenas as contas Analíticas e que possuam o mesmo código da empresa do vínculo.

A **"Conta contábil"**, é um campo alimentado automaticamente pelo sistema que identifica a Conta Contábil a qual pertence aquele grupo de contas externas.

O campo **"Saldo da conta vinculada"**, nesta aba, deve ser preenchido para informar o saldo associado à conta vinculada. Ele possibilita indicar o saldo para geração do Registro l157 quando este for vinculado em mais de uma conta contábil no registro l155 ou quando esse registro foi gerado por centro de resultado.

Quando este campo for preenchido, o **"Indicador da situação do saldo inicial"** será ativado para seleção, permitindo escolher uma das seguintes opções:

- **D** - Devedor
- **C** - Credor

É importante observar que, caso o campo **"Saldo da conta vinculada"** seja preenchido, o preenchimento do **"Indicador da situação do saldo inicial"** se torna obrigatório. Caso não o faça, o sistema exibirá a seguinte mensagem de validação:

**“Campo Indicador da situação do saldo inicial é obrigatório se no campo Saldo da conta vinculada estiver preenchido.”**

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607574-Vincula%C3%A7%C3%A3o-de-Contas-Cont%C3%A1beis-Externas#top)

## Aba Máscara Conta Externa

![Imagem 6: Aba Máscara Conta Externa](https://ajuda.sankhya.com.br/hc/article_attachments/360073008974)

Por meio dessa aba, defina a máscara que será utilizada para o cadastro das contas externas.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607574-Vincula%C3%A7%C3%A3o-de-Contas-Cont%C3%A1beis-Externas#top)

Veja também:

[Empresas da Contabilidade - Preferências](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607994-Empresa)

[Importação de Lotes com base no ECD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116053)

[Importação do Plano de Contas com base no ECD](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044607434)
