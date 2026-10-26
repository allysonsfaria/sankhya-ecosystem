---
id: "21517622604567"
titulo: "Autorização de Customizações"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/21517622604567-Autoriza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es"
trilha: "Manual do Produto > Plataforma e Integrações > Plataforma"
atualizado_em: "2026-10-07T17:58:23Z"
rotulos: ["Configuração", "Segurança", "Customização", "Plataforma Sankhya", "Administração do Sistema"]
---

# Autorização de Customizações

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42315444868631) Módulo: Configurações > Avançado  
```

---

![Imagem 2: Informações essenciais acerca da tela:](https://ajuda.sankhya.com.br/hc/article_attachments/22674301729943) **Informações essenciais acerca da tela:**

Os recursos e ferramentas descritos neste artigo estão disponíveis nas seguintes versões do **Sankhya Om**:

- Versão 4.21 em diante com data de compilação igual ou superior a 22 de fevereiro de 2024, independente da build;
- Versão 4.23 com build 193 ou superior, independente da data de compilação.

![Imagem 3: Qualquer alteração na customização resulta na revogação da autorização, exigindo que o processo seja refeito para essa…](https://ajuda.sankhya.com.br/hc/article_attachments/22674307980567) Qualquer alteração na customização resulta na revogação da autorização, exigindo que o processo seja refeito para essa customização específica.

---

A Plataforma Sankhya possui muitos recursos de customização flexíveis e poderosos, e é reconhecida no mercado por essa e outras características únicas.

Além disso, já dispõe de uma gama de recursos de segurança que, aliados às melhores práticas de segurança corporativa, são fundamentais para auxiliar o Administrador do Sistema a garantir a integridade do ambiente.

Em compromisso com a segurança e o compliance, e cientes do potencial impacto das customizações, fora adicionada uma camada adicional de segurança: a tela Autorização de Customizações. Essa medida fortalece ainda mais a proteção, proporcionando tranquilidade aos administradores e usuários quanto à integridade e segurança do sistema.

A principal finalidade desta ferramenta é conceder ao Administrador do Sistema um controle total sobre as ações que podem ser realizadas em seu ambiente.

Independentemente do usuário que tenha criado ou importado a customização no Sistema, (incluindo o **SUP**), nenhuma ação será executada sem uma liberação efetiva.

![Imagem 4: Independentemente do usuário que tenha criado ou importado a customização no Sistema, (incluindo o SUP ) , nenhuma ação…](https://ajuda.sankhya.com.br/hc/article_attachments/21517616785687)

A liberação é realizada pelo usuário SUP (ou por quem ele designar), através de um Código de Segurança aleatório, automaticamente gerado pelo Sistema e enviado para o e-mail do Administrador do Sistema.

Esse código tem validade de 10 minutos e pode ser utilizado para liberar um ou mais itens do mesmo tipo. Cada aba na tela corresponde a um tipo específico de customização, assim, o código gerado em uma aba está limitado a liberar itens pertencentes àquela categoria.

Além disso, os códigos são únicos para cada ambiente, o que impede o uso cruzado entre diferentes ambientes.

| Funcionalidades da tela |
| --- |
| [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/21517622604567-Autoriza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es#configura%C3%A7%C3%A3o) |
| [Fluxo básico de liberação](https://ajuda.sankhya.com.br/hc/pt-br/articles/21517622604567-Autoriza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es#fluxo) |
| [Práticas recomendadas para este processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/21517622604567-Autoriza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es#pr%C3%A1ticas) |
| [Cuidados necessários no processo](https://ajuda.sankhya.com.br/hc/pt-br/articles/21517622604567-Autoriza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es#cuidados) |

### Configurações

Este novo recurso é ativado por meio de uma configuração no ambiente de execução (Servidor Wildfly), utilizando a seguinte flag:

```
-Dsnk.use.action.auth=true
```

Assim como as outras flags, essa é informada no arquivo de configurações:

```
WILDFLY_INSTALL/bin/standalone.conf (Linux)

WILDFLY_INSTALL/bin/standalone.conf.bat (Windows)
```

Para fortalecer a segurança do processo, é crucial definir a lista de endereços de e-mail para os quais o Sistema enviará o Código de Verificação.

Essa configuração deve ser realizada no próprio Servidor de Aplicações. Para acessá-lo, são necessários o nome de usuário e senha do Sistema Operacional, os quais são de responsabilidade do cliente ou do administrador da infraestrutura onde o sistema está hospedado.

O sistema busca automaticamente esse arquivo na pasta home do usuário de execução do sistema operacional, tanto no Linux quanto no Windows.

Em casos onde o usuário de execução em uso é o padrão (mgeweb), o caminho completo para o arquivo será:

```
/home/mgeweb/sankhyaconf/[BASE]/admin/mail.cfg
```

**Observação:** [BASE] é o nome do usuário de banco de dados utilizado na aplicação.

Caso tenha instalado mais de um ambiente na mesma máquina servidora, haverá **“N”** arquivos, um para cada base. Por exemplo, se o nome de usuário do banco de dados for **"skprod"**, tem-se:

```
/home/mgeweb/sankhyaconf/skprod/admin/mail.cfg
```

Se desejar que a estrutura esteja em uma pasta base diferente, basta especificar essa pasta na propriedade **"snk.auth.folder"**, no mesmo arquivo de configuração mencionado anteriormente, da seguinte forma:

```
-Dsnk.auth.folder=/home/mgeweb/xpto
```

Desta forma, o arquivo será gravado no seguinte caminho:

```
/home/mgeweb/xpto/sankhyaconf/[BASE]/admin/mail.cfg
```

Caso esse caminho não exista, basta criar da forma tradicional do **Sankhya Om**, como **"mkdir"** no Linux. O arquivo é no formato texto e pode ser criado com qualquer editor disponível no sistema operacional. Nele, deve-se informar um ou mais e-mails (um por linha) que será usado no processo de liberação, assim:

- tech@minhaempresa.com.br;
- suporte@minhaempresa.com.br.

Esse arquivo pode ser modificado mesmo com o sistema em execução, e as modificações terão efeito já no próximo uso.

Não há por enquanto forma de alterar esse arquivo pela aplicação Sankhya.

Os e-mails cadastrados aqui devem ser de funcionários de confiança da empresa ou do provedor de serviços de nuvem. Nunca coloque e-mails de terceiros.

Esse novo recurso não grava informações no Banco de Dados. Isso significa que as liberações realizadas em um ambiente não funcionam em outro, independentemente de ser um ambiente de TESTE e outro de PRODUÇÃO.

![Imagem 5: Ambientes diferentes, liberações independentes.](https://ajuda.sankhya.com.br/hc/article_attachments/22674307980567) Ambientes diferentes, liberações independentes.

O ambiente de TESTE geralmente é um backup que um dia foi PRODUÇÃO, portanto sugerimos fortemente que esse recurso seja ligado em todos os ambientes.

O servidor de aplicações da empresa é um ambiente de acesso restrito, dado a sensibilidade de informações presentes, como configurações, dados, chaves de criptografia e outros. Sendo assim, a segurança do processo depende fortemente da boa gestão de acessos a essa máquina.

Durante o processo de implementação do EIP, é comum a criação de diversas customizações na Plataforma, e consideramos boa prática que isso seja feito em um ambiente de teste cujas liberações realizadas não terão validade no ambiente de produção.

O momento do GO LIVE é uma excelente oportunidade para revisar tudo e conferir quais e-mails estão presentes no arquivo de configuração, além da troca das senhas dos usuários da máquina servidora, incluindo o root.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/21517622604567-Autoriza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es#top)

### Fluxo básico de Liberação

Com a tela aberta, será possível visualizar os itens existentes em cada uma das abas, sem a necessidade de clicar em qualquer botão.

Antes de liberar uma aba, é fundamental analisar cuidadosamente cada item quanto à sua segurança, seguindo os princípios a seguir:

**(1)** Não realize a liberação de itens cuja finalidade seja desconhecida;

**(1)** Não faça a liberação de itens com descrições suspeitas.

Em caso de dúvida, libere os itens conforme julgar necessário.

Na barra superior da aba, utilize o campo **"Buscar itens"** para localizar um item pela **"Descrição"**, ou aplique o filtro de **"Situação"**, para visualizar itens com as seguintes características:

- Todos;
- Pendentes;
- Liberado;
- Proibido.

Após selecionada a lista de itens a serem liberados, clique no botão ![Imagem 6: Após selecionada a lista de itens a serem liberados, clique no botão "Gerar código de liberação" e aguarde o envio do…](https://ajuda.sankhya.com.br/hc/article_attachments/22676326016919) **"Gerar código de liberação"** e aguarde o envio do código por e-mail.

Caso não receba o e-mail em tempo hábil, verifique a configuração dos e-mails de administradores, para isso acesse a seção [Configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/21517622604567-Autoriza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es#configura%C3%A7%C3%A3o) deste artigo.

Com o código de liberação em mãos, selecione, na grade, os itens a serem liberados e clique no botão ![Imagem 7: Com o código de liberação em mãos, selecione, na grade, os itens a serem liberados e clique no botão " Informar Código"…](https://ajuda.sankhya.com.br/hc/article_attachments/22676316827543) **"Informar Código"**.

 Existem dois padrões do sistema para selecionar um ou mais itens da grade, escolha um:

- Mantenha pressionada a tecla **"Shift"** e utilize as setas de navegação de seu teclado, ou;
- Pressione a tecla **"CTRL"** e selecione as linhas com o mouse.

Esteja ciente de que será possível repetir essa operação utilizando o mesmo código dentro do prazo de 10 minutos, que é o tempo de validade do código.

---

**![Imagem 8: Informações sobre o fluxo:](https://ajuda.sankhya.com.br/hc/article_attachments/22674301729943) Informações sobre o fluxo:**

Para que o e-mail com o código seja enviado ao Autorizador de Customizações, é necessário configurar a conta [SMTP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603194-Contas-SMTP) no sistema.

Clientes SaaS não precisam realizar a configuração da conta, basta abrir um chamado com a categoria SaaS > Solicitações > Definir e-mail de Autorização de Customizações e informar qual o e-mail do Autorizador de Customizações para que o cadastro seja realizado.

---

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/21517622604567-Autoriza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es#top)

### Cuidados necessários no processo

Os elementos customizados são programas desenvolvidos por terceiros que funcionam dentro da plataforma Sankhya, capazes de executar operações e modificar dados de uma maneira que torna difícil para o sistema determinar a legitimidade e segurança das alterações.

Portanto, o Responsável pelo Sistema só deve liberar para execução itens que ele considera seguros e provenientes de fornecedores confiáveis.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/21517622604567-Autoriza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es#top)

### Práticas recomendadas para este processo

A eficiência e a segurança dos processos são essenciais para garantir o bom funcionamento das operações. Para isso, é fundamental adotar práticas recomendadas que possam otimizar os procedimentos e mitigar possíveis riscos, no processo de Autorização de Customizações é necessário seguir as seguintes recomendações:

- Exigir do fornecedor a descrição funcional e uma apresentação do item funcionando em ambiente de desenvolvimento;
- Compreender os recursos aos quais o item tem acesso, como disco, rede e APIs externas, bem como suas funcionalidades de leitura e modificação de dados;
- Evitar a instalação de itens de origem desconhecida, que realizam acesso aleatório ao banco de dados ou que violem a política de restrição de acessos e integridade de dados da Plataforma Sankhya.

Estas são apenas algumas boas práticas, no entanto, cada empresa deve aplicar as regras de compliance que considere necessárias.

![Imagem 9: Em caso de dúvidas, entre em contato nos canais de atendimento oficiais.](https://ajuda.sankhya.com.br/hc/article_attachments/22674307994775) Em caso de dúvidas, entre em contato nos canais de atendimento oficiais.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/21517622604567-Autoriza%C3%A7%C3%A3o-de-Customiza%C3%A7%C3%B5es#top)
