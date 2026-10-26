---
id: "44013303753367"
titulo: "[TMS] - Componente Suframa com valor fixo nos componentes por rota"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013303753367--TMS-Componente-Suframa-com-valor-fixo-nos-componentes-por-rota"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:53:55Z"
rotulos: ["sync_hc", "lincros", "lincros_13432706", "sync_hash_3c471a450208"]
---

# [TMS] - Componente Suframa com valor fixo nos componentes por rota

**Menu**: Cadastros Gerais > Transportadoras > Negociações > Tabelas de Frete

**Objetivo**: Como cadastrar o componente suframa com valor fixo nos componentes por rota da tabela de frete

**Considerações**:

- É necessário ter cadastrada no TMS a tabela de fretes;
- Ter em mãos o código ou nome da tabela a ser alterada;

Segue abaixo os procedimentos:

1. Acessar o menu: Cadastros Gerais > Configurações de empresa > Componentes de Frete;
2. Verificar se o componente em questão já encontra-se cadastrado ou caso ainda não estiver, clicar na opção 'Novo';
3. Preencher os campos abaixo:

**Código**: Informar uma sigla para este componente;

**Tipo de Cálculo**: Selecionar o tipo de cálculo 'Frete';

**Nome**: Informar o nome deste componente;

**Fórmula de Cálculo**: Informar qual será a fórmula de cálculo, neste caso, como será valor fixo a fórmula será: return VALOR\_FIXO;

**Ordem de Exibição:** Informar qual será a ordem de exibição, por exemplo: 8;

**Código do Movimento**: Informar a sigla para o código deste componente, exemplo: SUFR;

4. Selecionar a onde este componente será apresentado, por exemplo: Totalizador, Utilizar nas Generalidades, Utilizar em Rotas;

5. Nos valores, selecionar quais serão os tipos de valores, neste caso, selecionar o 'valor mínimo' e o 'valor fixo';

6. Nos tipos de faixas, selecionar quais serão os tipos de faixas que este componente será calculado, neste exemplo: Peso Nominal, Valor da Mercadoria, Peso Excedente;

7. Com todas as informações preenchidas, clicar no botão 'Salvar';

8. Acessar o menu: Cadatros Gerais > Transportadora > Negociações > Tabelas de Frete;

9. Selecionar a tabela de frete no qual será adicionado este novo componente nos componentes da rota;

10. Acessar a aba 'Componentes por Rota';

11. Selecionar a rota desejada;

12. Selecionar a faixa para cálculo, neste exemplo: Valor da Mercadoria;

13. Clicar na opção 'Adicionar Componente';

14. Na coluna 'Disponíveis', localizar o componente 'Suframa';

15. Selecionar o mesmo para a coluna 'Existentes' através da seta '>';

16. Clicar em 'Adicionar';

17. Adicionar no componente Suframa o valor fixo desejado;

18. Caso o componente não estar disponível, o mesmo deverá ser adicionado no menu: Cadatros Gerais > Transportadoras > Transportadora (Empresa);

19. Localizar o cadastro da transportadora em questão;

20. Acessar a aba 'Componentes';

21. Clicar na opção '(+) Incluir´;

22. Preencher conforme exemplo abaixo:

![Imagem 1: 22. Preencher conforme exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44013328445975)

23. Clicar em 'Incluir';

24. Após será necessário recalcular os movimentos do pré-conhecimento em: Operacional > Documentos de despacho > Notas Fiscais;

25. Ao abrir a nota fiscal, clicar na aba 'Conhecimentos';

26. Selecionar o conhecimento em questão;

27. Acessar a aba 'Movimentos';

28. Clicar na opção 'Recalcular';

29. Verificar se o componente calculou corretamente, conforme exemplo abaixo:

![Imagem 2: 29. Verificar se o componente calculou corretamente, conforme exemplo abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/44013328579479)

Exemplo da tela de cadastro do componente Suframa

![Imagem 3: Exemplo da tela de cadastro do componente Suframa](https://ajuda.sankhya.com.br/hc/article_attachments/44013328747287)

![Imagem 4: Exemplo da tela de cadastro do componente Suframa](https://ajuda.sankhya.com.br/hc/article_attachments/44013328936215)

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
