---
id: "44013292103063"
titulo: "[TMS] - Importação do Certificado Digital"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44013292103063--TMS-Importa%C3%A7%C3%A3o-do-Certificado-Digital"
trilha: "Lincros > TMS > Cadastros - TMS"
atualizado_em: "2026-10-05T19:53:16Z"
rotulos: ["sync_hc", "lincros", "lincros_13432731", "sync_hash_9b45c65544e0"]
---

# [TMS] - Importação do Certificado Digital

**Menu**: Cadastros Gerais > Configurações de Empresa > Gerais > Certificado Digital

**Objetivo**: Instruir o usuário como importar corretamente o certificado digital

**Considerações**:

- Possuir o arquivo do certificado digital (extensão .pfx);
- Possuir a senha do certificado digital;

**Caminho (Windows)**

Para que você consiga importar o arquivo .pfx com a cadeia completa, ou seja, com todas informações inseridas no certificado, devem ser seguidos os seguintes passos em seu Windows;

Sendo assim é necessário importar o certificado na sua máquina primeiro para que depois este possa ser exportado com as informações suficientes para ser importado na plataforma Lincros;

Para isso, seguir os procedimentos abaixo:

1. Abra o Executar (comando Windows + R);
2. Digite o valor mmc;
3. Na janela que se abriu, acessar o menu Arquivo > Adicionar/remover snapin;
4. Na aba da esquerda, selecione o snapi-in "Certificados" e clique no botão central 'Adicionar > ';
5. Selecione a opção Minha conta de usuário e clique em 'Concluir' e em seguida em 'Ok';
6. Expandir a árvore de Certificados localizada à esquerda;
7. Selecione a aba “Pessoal”;
8. Acesse o menu Ação > Todas as tarefas > Clique em importar;
9. O Sistema vai abrir um assistente. Clique em avançar e em seguida selecione o Certificado (o formato do certificado deve ser .pfx) e clique em avançar;
10. Na próxima janela, informe a senha do certificado e marque o checkbox “Marcar esta chave como exportável. Isso possibilitará o backup e transporte das chaves posteriormente”. Como o texto diz se você não marcar esta opção o certificado não poderá ser exportado. Clique novamente em Avançar > Avançar e Concluir;
11. Exportar Certificado;
12. Após ser importado, seu certificado vai para a aba Pessoal > Certificados. Clique sobre o certificado que deseja exportar e vá para Ações > Todas as tarefas > Exportar;
13. Clique em avançar;
14. Marque a opção 'Sim, exportar a chave privada' e clique em avançar;
15. Na janela seguinte marque o checkbox “Exportar todas as propriedades estendidas" e clique em Avançar;
16. Marque o checkbox senha, informe a senha e em seguida confirme a mesma senha e clique em Avançar;
17. Na próxima janela, selecione o local onde o arquivo será salvo. Após isso pode concluir o assistente;
18. PRONTO! Feito isso está pronto e você já pode importar o certificado exportado para a plataforma Lincros;

## Configurando dentro do TMS

1. No TMS acesse o menu: Cadastros Gerais > Configurações de Empresa > Gerais > Certificado Digital e clique na opção 'Novo';
2. Nesta tela, deve-se arrastar o certificado até o local indicado na tela ou selecionar o mesmo através do botão “Adicionar”;
3. Depois deve-se informar a senha;
4. Clicar no botão “Importar”;
5. Se o certificado estiver correto e dentro dos padrões do ICP Brasil, as informações do mesmo serão preenchidas automaticamente. Também serão vinculadas no cadastro todas as unidades que possuam o mesmo cnpj raiz do certificado importado, pode-se remover ou adicionar unidades para vincular as mesmas ao certificado;
6. Não é possível vincular mais de um certificado para a mesma unidade, nem importar certificados que sejam de uma empresa diferente da empresa corrente.

## Notificação de data de expiração

É disparado um e-mail de notificação aos e-mails configurados no parâmetro de empresa  'destinatarioNotificacaoVencimentoCertificado', alertando com 30, 5, e 1 dia de antecedência da data final de vigência.

**Obs.:** Os campos que aparecem em vermelho são de preenchimento obrigatório.

  "Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
