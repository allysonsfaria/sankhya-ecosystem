---
id: "360044109794"
titulo: "Unknown user name or password"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044109794-Unknown-user-name-or-password"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-10-08T11:47:42Z"
rotulos: ["aplicativo licença", "licenca.dat", "Configuração", "MGE", "Segurança", "Financeiro", "Solução de problemas", "Acesso ao MGE", "Senha do Banco de Dados", "Erro", "Artigo atualizado KCS", "Plataforma - KCS"]
---

# Unknown user name or password

Unknown user name or password.
Login failed for user 'SANKHYA'.
Login incorrect.
Alias: DBNSiade.

### SITUAÇÃO

Ao tentar acessar o MGE, o sistema apresenta erro de conexão ou autenticação. O usuário realizou a troca da senha do usuário sankhya diretamente no banco de dados e criou um novo arquivo LICENSE.DAT, porém ainda não consegue efetuar login no sistema.

### SOLUÇÃO

Considere o comportamento da aplicação, conforme abaixo:

**(1)** Solicite que a área de TI ou administrador de banco de dados revise a senha do banco, seguindo as seguintes considerações para a senha:

- Máximo de 10 caracteres;
- Uso apenas de caracteres minúsculos;
- Não pode ser utilizado o número 0;
- São aceitos apenas alguns caracteres especiais: !, \*, $, | e &.

**(2)** Depois de usar uma senha dentro do padrão, gere um novo arquivo LICENSE.DAT e insira este arquivo dentro da pasta do executável do MGE.

Caso utilize o Sankhya W, refaça a conexão com o banco de dados pelo gerenciador de pacotes e atualize a senha no arquivo de configuração do SAS (SAS.CFG).

[**Clique aqui**](https://ajuda.sankhya.com.br/hc/pt-br/article_attachments/360060111454) para baixar o License.zip

**(3)** Caso o problema persista, verifique as permissões do diretório de instalação do sistema:

- Localize o executável do MGE no diretório de instalação;
- Clique com o botão direito do mouse sobre o executável e selecione a opção **"Propriedades"**;
- Acesse a aba **"Compatibilidade"**;
- Marque a opção **"Executar este programa como administrador"**;
- Clique em **"Aplicar"** e em seguida em **"OK"** para salvar as configurações.

### CAUSA

Ocorre quando a senha do banco de dados está incorreta. A senha padrão é **"tecsis"**; caso o cliente altere essa senha, é necessário gerar o arquivo **license.dat** na pasta onde estão os executáveis do MGE.

Também pode ocorrer devido a restrições de permissão no sistema operacional, que impedem o MGE de acessar corretamente os arquivos de configuração e de licença após alterações no ambiente.

### OBSERVAÇÃO

Veja também artigo relacionado: [Não conectado ao ORACLE](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616613)
