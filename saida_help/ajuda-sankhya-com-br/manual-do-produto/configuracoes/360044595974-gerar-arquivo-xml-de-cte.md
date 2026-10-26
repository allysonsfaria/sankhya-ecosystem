---
id: "360044595974"
titulo: "Gerar Arquivo XML de CTe"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044595974-Gerar-Arquivo-XML-de-CTe"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-08-28T16:53:46Z"
rotulos: ["CT-e", "manual", "br.com.sankhya.com.rotinas.gerararquivoxmlcte", "Gerar Arquivo XML de CTe manual", "XML", "SEFAZ", "Download de Arquivos XML de CT-e: Instruções e Filtros", "Documentos Eletrônicos", "Serviço Tomado", "Emissão Própria"]
---

# Gerar Arquivo XML de CTe

Através desta tela, é possível realizar o download dos arquivos XML de CT-e que encontram-se armazenados. Estes arquivos poderão estar relacionados ao XML de CT-e Emitidos, Serviços Tomados ou Cancelados.

Em relação ao campo **"Empresa"**, seleciona-se a empresa que se deseja realizar o download, podendo esta ser pesquisada diretamente por seu número de registro ou pela opção de **"Pesquisa"**.

Todos os campos desta tela são filtros para que o usuário selecione o CT-e desejado para realizar o download, sendo que, estes filtros deverão seguir as seguintes regras:

- Ao ser preenchido o campo **"Chave CT-e"** todos os demais campos ficarão desabilitados.
- Preenchendo o campo **"Número da nota"** todos os campos ficarão indisponíveis, com exceção do campo **"Série"**.
- De outra forma, ao informar a data referente ao campo **"Período"**, os campos Chave CT-e, Número da nota e Série não se encontrarão disponíveis.

No campo Período, informa-se a data inicial e a data final da emissão do lote.

**Importante:** é necessário informar o período da emissão do lote quando os campos Número da Nota ou Chave CT-e não encontrarem-se preenchidos, visto que, trata-se de um campo obrigatório. Caso não seja informado este período, não será possível realizar o download do arquivo. Sendo assim, o sistema apresentará o seguinte aviso:

**"O Período é obrigatório quando o Número da nota ou Chave CT-e não são informados".**

Caso o usuário insira as informações nos campos Empresa e Período, ao realizar o download, será gerado um arquivo de lote de notas compactado com todos os XML's.

Informa-se no campo Chave CT-e a chave que irá compor o filtro. Desta forma, bastará que seja inserida esta informação para que o sistema selecione a nota a ser exportada, uma vez que, cada nota possui apenas um único número de chave.

Nos campos Número da Nota e Série serão inseridos o número e a série da nota desejada.

**Observação:** sendo informado apenas o número da Série sem informar o Número da Nota, será apresentada a seguinte mensagem:

**"Ao informar a série a nota deve ser informada".**

Ao considerar o campo **"Tipo de Período"**, deverá ser selecionado qual o tipo de período da nota a ser utilizado no filtro, sendo assim, tem-se disponibilizadas as seguintes opções:

- Negociação;
- Movimento;
- Faturamento;
- Entrada/Saída.

Em relação ao campo **"Tipo de Arquivo"**, informa-se o tipo de arquivo para realizar-se o download. Desta forma, pode-se selecionar uma das opções a seguir:

- Emissão Própria;
- Serviço Tomado;
- Ambos.

Ao selecionar a opção **"Serviço Tomado"**, o sistema não aceitará as datas de movimento ou faturamento e, desta forma, emitirá o seguinte aviso:

**"As datas de Movimento e Faturamento poderão ser utilizadas apenas para o Tipo de Arquivo igual a Emissão Própria".**

Sendo assim, ao selecionar esta opção, o sistema considerará a data de negociação para aplicação deste filtro.

Ao habilitar a marcação **"Canceladas"** será gerado o XML apenas dos CT-e's que foram cancelados.

**Observação:** selecionando a marcação acima, o campo Tipo de Arquivo será desabilitado.

Por fim, não sendo informado nenhum tipo de filtro nesta tela e acionando o botão **"Download"**, o sistema emitirá a seguinte mensagem:

**"Parâmetros para download não foram informados".**

## Parâmetros que influenciam nesta rotina

O parâmetro **"Gerar XML de aprovação e cancelamento? - GERAXMLAPROVCAN"** está vinculado à marcação Canceladas, sendo que, quando este encontrar-se desligado, será realizado o download apenas do XML de cancelamento. Por outro lado, habilitando-se este parâmetro, será feito também o download do XML de aprovação.

Quando o parâmetro **"Aplicar validação de XML no download de CT-e? - VALIDXMLDOWNCTE"** estiver habilitado, será executado um método para validação do XML de envio da nota. Caso o mesmo não seja validado, será gerado o protocolo de autorização novamente a partir do XML da nota.
