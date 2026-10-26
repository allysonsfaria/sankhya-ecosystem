---
id: "44010190042391"
titulo: "[TMS] Erros na importação de EDI"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010190042391--TMS-Erros-na-importa%C3%A7%C3%A3o-de-EDI"
trilha: "Lincros > TMS"
atualizado_em: "2026-10-05T18:31:48Z"
rotulos: ["sync_hc", "lincros", "lincros_13432070", "sync_hash_30daaa6c7ac2"]
---

# [TMS] Erros na importação de EDI

Todos os arquivos importados para o TMS geram informações de logs que ficam armazenadas na plataforma. Essas informações nos auxiliam a identificar erros e motivos que levaram esses arquivos a não serem importados. Na imagem abaixo, por exemplo, notamos que alguns arquivos estão com um ícone vermelho com um “X”, que indica que o documento foi processado com erros, e o outro com um ícone verde e com um sinal de “check”, indicando que o documento foi processado com sucesso.

![Imagem 1: Todos os arquivos importados para o TMS geram informações de logs que ficam armazenadas na plataforma. Essas…](https://ajuda.sankhya.com.br/hc/article_attachments/44010190301719)

Clicar no código da linha que está em vermelho, e indo na aba “Erros” podemos visualizar os motivos das críticas:

![Imagem 2: Clicar no código da linha que está em vermelho, e indo na aba “Erros” podemos visualizar os motivos das críticas:](https://ajuda.sankhya.com.br/hc/article_attachments/44010159667095)

Na listagem abaixo temos as críticas que podem ser apresentadas na importação de um EDI, e uma explicação do porquê são apresentadas:

**Erro**: Conhecimento de transporte XXXXX já possui chave vinculada [XXXXX].

**Explicação**: Se trata da importação de um CONEMB quando, na verdade, já houve a importação do XML do CT-e. A importação do XML cria o CT-e com chave de acesso, tratando-se de um documento eletrônico com validação no site da Sefaz, já a importação do CONEMB realiza a criação do CT-e no sistema sem chave de acesso e validação na Sefaz. A mensagem nada mais é do que um aviso de que já foi importado o XML antes do CONEMB e por isso o sistema não processa o arquivo. Ressaltamos que o ideal é a utilização de somente uma das formas de criação de CT-e, onde uma exclui a necessidade de importação da outra.

![Imagem 3: Explicação : Se trata da importação de um CONEMB quando, na verdade, já houve a importação do XML do CT-e. A importação…](https://ajuda.sankhya.com.br/hc/article_attachments/44010159926679)

**Erro**: Conhecimento de transporte XXXXX encontrado, contudo a nota fiscal presente no arquivo de fatura não está vinculada ao conhecimento.

**Explicação**: Na posição 4 do registro 353 (C C O - CONHECIMENTOS EM COBRANÇA) temos a série do CTe, e na posição 19 temos o número do CTe. Já no registro 354 (C N F - NOTAS FISCAIS EM COBRANÇA NO CONHECIMENTO) na posição 4 temos a série e na posição 7 temos o número da NFe. Deve-se verificar se os dados (número + série) da nota fiscal informada no EDI está conforme os dados da nota no sistema. Normalmente a série da nota acaba sendo enviada incorretamente no EDI, causando o erro abaixo.

![Imagem 4: Explicação : Na posição 4 do registro 353 (C C O - CONHECIMENTOS EM COBRANÇA) temos a série do CTe, e na posição 19…](https://ajuda.sankhya.com.br/hc/article_attachments/44010178866199)

**Erro**: Conhecimento não localizado com a transportadora XXXXX para o documento [XXXXX].

**Explicação**: Significa que a nota fiscal referenciada não está com a mesma transportadora que se refere o arquivo OCORREN. Ou seja, a transportadora informada no OCORREN é uma, mas a nota que consta no sistema está vinculada a outra transportadora.

![Imagem 5: Explicação : Significa que a nota fiscal referenciada não está com a mesma transportadora que se refere o arquivo…](https://ajuda.sankhya.com.br/hc/article_attachments/44010149598871)

**Erro:** Nota fiscal [XXXXX] não localizada.

**Explicação:** Significa que a nota fiscal referenciada no EDI não consta no TMS, portanto, deve-se importar o XML do documento e, posteriormente, reimportar (ou reprocessar) o EDI.

![Imagem 6: Explicação: Significa que a nota fiscal referenciada no EDI não consta no TMS, portanto, deve-se importar o XML do…](https://ajuda.sankhya.com.br/hc/article_attachments/44010179288471)

**Erro:** Já existe ocorrência com ação finalizadora ou entrega no documento fiscal XXXXX.

**Explicação:** Significa que está importando um OCORREN para dar baixa no documento fiscal, contudo, este documento já recebeu uma ocorrência finalizadora (ou de entrega) e por este motivo o sistema não processará aquela ocorrência.

![Imagem 7: Explicação: Significa que está importando um OCORREN para dar baixa no documento fiscal, contudo, este documento já…](https://ajuda.sankhya.com.br/hc/article_attachments/44010149901335)

**Erro:** Conhecimento de transporte XXXXX já associado a fatura XXXXX.

**Explicação:** Significa que está importando um DOCCOB, contudo, o CT-e referenciado já está vinculado a outra fatura, portanto, o sistema não processará com sucesso este arquivo.

![Imagem 8: Explicação: Significa que está importando um DOCCOB, contudo, o CT-e referenciado já está vinculado a outra fatura,…](https://ajuda.sankhya.com.br/hc/article_attachments/44010150095511)

**Erro:** O tomador do serviço não é uma pessoa cadastrada [XXXXX].

**Explicação:** Aqui o sistema tenta recuperar a unidade passando o CNPJ e, caso não esteja cadastrado no sistema, retorna a crítica! Ou seja, não existe nenhuma unidade da empresa cadastrada com o CNPJ informado.

![Imagem 9: Explicação: Aqui o sistema tenta recuperar a unidade passando o CNPJ e, caso não esteja cadastrado no sistema, retorna…](https://ajuda.sankhya.com.br/hc/article_attachments/44010192033815)

**Erro:** Conhecimento de transporte não encontrado: XXXXX.

**Explicação:** Significa que está importando um DOCCOB que contem CT-es que não foram encontrados no TMS. Portanto, deve-se importar o XML dos documentos (CT-es) e, posteriormente, importar (ou reprocessar) o arquivo EDI.

![Imagem 10: Explicação: Significa que está importando um DOCCOB que contem CT-es que não foram encontrados no TMS. Portanto,…](https://ajuda.sankhya.com.br/hc/article_attachments/44010166599191)

**Erro:** Fatura XXXXX já foi aceita, conferida ou paga.

**Explicação:** Significa que está importando um DOCCOB no qual a transportadora cita um número de fatura que já se encontra aceita, conferida ou paga no TMS. Deve-se entender a situação com a transportadora que emitiu o documento.

![Imagem 11: Explicação: Significa que está importando um DOCCOB no qual a transportadora cita um número de fatura que já se…](https://ajuda.sankhya.com.br/hc/article_attachments/44010211428375)

**Erro:** Transportadora não localizada.

**Explicação:** A transportadora informada no documento (EDI) não consta na base de dados do TMS, portanto, é necessário cadastrá-la para posteriormente importar o EDI.

![Imagem 12: Explicação: A transportadora informada no documento (EDI) não consta na base de dados do TMS, portanto, é necessário…](https://ajuda.sankhya.com.br/hc/article_attachments/44010192632215)

**Erro:** CT-e sem chave de acesso após importação via CONEMB/EDI.

**Explicação:** O CONEMB, por ser um formato EDI com layout fixo (PROCEDA), não possui campo para a chave de acesso do CT-e eletrônico — ele simplesmente não carrega essa informação, mesmo quando o CT-e é válido. Já quando o CT-e é importado pelo XML emitido pela SEFAZ, a chave de acesso vem dentro do próprio arquivo e é registrada normalmente no TMS. Se um CT-e ficou sem chave por ter entrado via CONEMB, a correção é reimportar o XML desse mesmo CT-e. Atenção: o sistema não permite sobrescrever dados de CT-es que já estão integrados ou aguardando integração — nesses casos, é necessário primeiro reverter a integração e só então importar o XML, ou o sistema devolve o CT-e para a fila de integração automaticamente e volta a bloquear a reimportação.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
