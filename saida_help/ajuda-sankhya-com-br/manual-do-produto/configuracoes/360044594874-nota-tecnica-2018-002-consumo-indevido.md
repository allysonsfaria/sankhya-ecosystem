---
id: "360044594874"
titulo: "Nota Técnica 2018.002 - Consumo Indevido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594874-Nota-T%C3%A9cnica-2018-002-Consumo-Indevido"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:44:27Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Nota Técnica 2018.002 - Consumo Indevido manual", "Regras para Consumo Indevido - Nota Técnica 2018.002", "Erro", "Documentos Eletrônicos"]
---

# Nota Técnica 2018.002 - Consumo Indevido

O uso indevido de serviços pode comprometer a estabilidade dos Web Services, resultando na saturação dos recursos, o que possibilita o ambiente autorizador inoperante, além de que, podem ser interpretadas como ataques aos recursos de processamento e rede.

A Nota Técnica 2018.002 foi criada para tratar este tipo de uso, o que poderá resultar em regras e penalizações para consumo indevido. No entanto, existem (têm) fatores principais como os limites de tentativas e o tempo de bloqueio do usuário, que podem ser alterados por cada Sefaz estadual. Por padrão, caso a UF opte por manter os valores padrões estabelecidos pela Nota Técnica 2018.002, a Rejeição por Consumo Indevido ocorrerá quando:

- Uma NFe ou NFC-e for enviada mais de 30 vezes e apresentar o mesmo status de rejeição;
- Um evento apresentar 20 vezes a mesma rejeição;
- Inutilização enviada mais de 20 vezes e apresentar a mesma rejeição;
- Uma NFe for consultada mais de 10 vezes em 1 hora;
- Um recibo for consultado mais de 40 vezes em 1 hora.

---

### Limite de Envio de NFe / NFC-e

A tabela RejeiçãoNfe (TGFREJNFE) armazenará o número da nota, o código da rejeição retornado, a quantidade de vezes que foi recebida essa mesma rejeição, e uma hash (assinatura) do xml rejeitado. Tem-se como exemplo uma rejeição relacionada com a Inscrição Estadual inválida de determinada empresa, e é apresentada uma rejeição anterior a esta, e não havendo uma correção do erro, um novo registro será criado na tabela RejeiçãoNfe.

Caso uma rejeição seja de fato encontrada, têm-se as possibilidades:

Se a URL deste serviço estiver configurada no arquivo **"url-webservices.xml"** contendo o atributo **"maxRejeicoesRepetidasPorDocumento"**, o sistema irá consultar o máximo de rejeições por documento permitidas para esse serviço, e irá comparar com o campo **"CODREJEICAO"** da tabela RejeicaoNfe, neste caso pode ocorrer duas situações:

Caso o número de rejeições esteja dentro do limite e você não altere a nota, o sistema exibirá um pop-up com a mensagem:

**"A sua nota não sofreu alterações no xml e foi encontrada 1 rejeição de código 209 para essa mesma NF-e. Deseja continuar mesmo assim?"**

Ao clicar em **"Não"**, o sistema não prosseguirá com o evento. Caso você selecione o botão **"Sim"**, será apresentada a mesma rejeição e o registro da tabela será atualizado com a QTDREJEICOES atualizada.

Caso o número de rejeições tenha atingido o limite, a mensagem a seguir será exibida:

**"O serviço não será finalizado, pois o limite de rejeições foi alcançado. Foram 2 repetições de rejeições 209 para o mesmo xml dessa NF-e."**

**Observação:** fica a critério de cada UF bloquear o contribuinte permanentemente caso este ultrapasse 50 bloqueios de 1 hora. Sendo assim, este só conseguirá retornar às emissões com a aprovação da UF Autorizada.

---

### Limite de Envio de Eventos

Caso seja enviado determinado evento com a mesma rejeição mais de 20 vezes, o contribuinte ficará recebendo a rejeição 656 durante o período de 1 hora. Se o evento continuar a ser enviado, as regras da rejeição descritas no item acima devem ser utilizadas.

---

### Limite de Consulta por chave de acesso

Nesta situação, caso a consulta seja feita por meio da mesma chave de acesso por mais de 10 vezes dentro do período de 1 hora, o contribuinte receberá a rejeição 656 (Rejeição: consumo indevido pelo aplicativo da empresa). Após o período de 60 minutos, o contribuinte poderá realizar mais 10 consultas com uma mesma chave.

**Nota:** a verificação do colaborador ocorrerá da mesma maneira dos itens aqui já citados.

---

### Limite de consulta por recibo

Se o mesmo recibo for consultado por mais de 40 vezes dentro do período de 1 hora, o contribuinte ficará durante 60 minutos recebendo a rejeição 656, após este período o colaborador poderá realizar mais 40 minutos de um mesmo objeto.

---

### Limitar Outros Serviços

Caso sejam feitas mais de 40 requisições repetidas em um webservice não relacionado nos itens citados acima, o contribuinte ficará uma hora recebendo a rejeição 656. A definição do contribuinte seguirá sendo a mesma dos anteriores citados.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594874-Nota-T%C3%A9cnica-2018-002-Consumo-Indevido#top)
