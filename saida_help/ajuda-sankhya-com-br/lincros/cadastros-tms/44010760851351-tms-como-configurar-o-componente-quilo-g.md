---
id: "44010760851351"
titulo: "[TMS] - Como configurar o componente quilo garantia na tabela de fretes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010760851351--TMS-Como-configurar-o-componente-quilo-garantia-na-tabela-de-fretes"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T18:45:45Z"
rotulos: ["sync_hc", "lincros", "lincros_13432649", "sync_hash_526cd19b6897"]
---

# [TMS] - Como configurar o componente quilo garantia na tabela de fretes

**Menu**: Cadastros gerais > Transportadoras > Negociações > Tabelas de frete

**Objetivo**: Como realizar a configuração do componente quilo garantia para que seja calculado na tabela de fretes

**Considerações**:

- Possuir a tabela de fretes deferida e com data de vigência informada cadastrada no TMS; Caso tiver dúvidas, consultar o artigo [[TMS] - Cadastro de tabela de fretes via tela do sistema](https://intercom.help/ajudalincros/pt-BR/articles/13432703-tms-cadastro-de-tabela-de-fretes-via-tela-do-sistema)

Abaixo segue os procedimentos:

1. Na tabela de fretes na aba 'Componentes por Rota', selecionar a(as) rota(as) desejadas;
2. Nestas rotas devem haver duas faixas para cálculo, uma de 'Valor da Mercadoria' (0,0000 à 9.999.999.999.999,0000) e outra de 'Peso Nominal' (0,0000 à 9.999.999.999.999,0000), conforme exemplo abaixo:

![Imagem 1: Nestas rotas devem haver duas faixas para cálculo, uma de 'Valor da Mercadoria' (0,0000 à 9.999.999.999.999,0000) e…](https://ajuda.sankhya.com.br/hc/article_attachments/44010739561623)

3. Na fórmula de cálculo 'Valor de Mercadoria', deve ter o componente AdValorem, com o campo 'Percentual' preenchido com o percentual informado na tabela de fretes enviadas pela transportadora, e o campo Valor Mínimo preenchido com o frete mínimo informado na Tabela;

![Imagem 2: 3. Na fórmula de cálculo 'Valor de Mercadoria', deve ter o componente AdValorem, com o campo 'Percentual' preenchido…](https://ajuda.sankhya.com.br/hc/article_attachments/44010745205399)

4. Na fórmula de cálculo do 'Peso Nominal' deve ter o componente 'Frete Peso' apenas com o campo 'Valor Fixo' preenchido com o valor informado da tabela na coluna Frete Kg Garantia;

![Imagem 3: 4. Na fórmula de cálculo do 'Peso Nominal' deve ter o componente 'Frete Peso' apenas com o campo 'Valor Fixo'…](https://ajuda.sankhya.com.br/hc/article_attachments/44010761309079)

5. Na aba 'Generalidades', deve-se inserir o componente 'Compara Frete Peso/ Frete Valor'. Com esse componente, sempre será considerado no pré-conhecimento o maior valor entre o calculado do Frete Peso e Frete Valor;

![Imagem 4: 5. Na aba 'Generalidades', deve-se inserir o componente 'Compara Frete Peso/ Frete Valor'. Com esse componente, sempre…](https://ajuda.sankhya.com.br/hc/article_attachments/44010765578519)

6. Caso houver necessidade, a tabela pode ficar com o status de 'Aguardando Aprovação', para que sejam realizados os testes de cálculo na 'Calculadora de Fretes', disponível em: Planejamento Logístico > Seleção de Transportadora > Calculadora de Frete;

Abaixo segue um exemplo da tabela de fretes que a transportadora envia para o embarcador:

![Imagem 5: Abaixo segue um exemplo da tabela de fretes que a transportadora envia para o embarcador:](https://ajuda.sankhya.com.br/hc/article_attachments/44010790519831)

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
