---
id: "26322304673943"
titulo: "Assistente de Melhores Práticas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26322304673943-Assistente-de-Melhores-Pr%C3%A1ticas"
trilha: "Assistente de Melhores Práticas > Conheça o Assistente"
atualizado_em: "2026-10-19T17:51:35Z"
rotulos: ["Configuração", "Rotinas", "br.com.sankhya.turnkey.cfg.melhorespraticas", "Assistente de Melhores Práticas", "configurações do EIP", "Sankhya", "Implantação", "ERP", "Melhores Praticas"]
---

# Assistente de Melhores Práticas

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/26400994719383) Módulo: Configurações > Rotinas             ![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/26401039849111) Versão disponível: A partir da 4.31b28
```

---

Esta tela permite configurar o sistema Sankhya de forma guiada e intuitiva, por meio de um passo a passo simplificado.

Em cada etapa, o sistema fornecerá as informações necessárias, e ao responder às perguntas apresentadas, as configurações serão aplicadas automaticamente. Esse processo agiliza a implementação, garantindo uma configuração otimizada e adaptada às necessidades específicas de cada cliente.

Benefícios ao utilizar esta tela:

- **Padronização dos processos empresariais:** promove maior eficiência e consistência ao garantir que os processos sejam uniformes em toda a empresa.
- **Segurança no uso do ERP:** assegura que as configurações estejam corretas, aumentando a segurança e confiabilidade no uso do sistema.
- **Identificação e adoção de melhores práticas de mercado:** contribui para que a empresa adote práticas mais eficientes e competitivas, alinhadas com os padrões do mercado.
- **Otimização do tempo e recursos:** automatiza configurações, facilitando o trabalho dos usuários e permitindo uma gestão mais ágil e eficiente dos recursos empresariais.

| Informações da Tela |
| --- |
| [Requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/26322304673943-Assistente-de-Melhores-Pr%C3%A1ticas#Requisitos) |
| [Configurações Iniciais](https://ajuda.sankhya.com.br/hc/pt-br/articles/26322304673943-Assistente-de-Melhores-Pr%C3%A1ticas#Configura%C3%A7%C3%B5esIniciais) |
| [Processos](https://ajuda.sankhya.com.br/hc/pt-br/articles/26322304673943-Assistente-de-Melhores-Pr%C3%A1ticas#Processos) |

---

## Requisitos

Para garantir a velocidade e efetividade da jornada de configurações iniciais nesta tela, é necessário que o responsável pela implantação se atente aos requisitos informados a seguir, com todos os arquivos e dados necessários previamente preparados:

### Ambiente

- Versão 4.31 ou superior;
- Licença do cliente devidamente vinculada.

### Cadastro de Empresas

Não é necessário cadastrar as empresas manualmente. O sistema consultará e realizará o cadastro a partir da licença instalada no ambiente.

Certificados digitais no modelo A1, com arquivo (extensão .pfx) e senha de acesso.

### Dados Bancários

Informações básicas das contas bancárias das empresas controladas pelo sistema:

- Banco;
- Número da Agência;
- Número da conta;
- Tipo da conta.

### Parceiros

Planilha modelo preenchida, conforme o formato e as instruções fornecidas no próprio modelo. [Clique aqui para baixar a planilha modelo](https://docs.google.com/spreadsheets/d/1gggJIXh9Fyhz6u3U9z-8MFOki98rB3Yw/edit?gid=1697159510#gid=1697159510).

Parceiros relacionados a Empresas e Bancos serão criados automaticamente pelos instaladores anteriores e não precisam constar na planilha.

### Produtos

Planilha modelo preenchida, de acordo com o formato e as orientações contidas no próprio modelo. [Clique aqui para baixar a planilha modelo](https://docs.google.com/spreadsheets/d/1hSmqM7245xCZKO0IdqQyG69FuVs6Z7gm/edit?gid=1060208211#gid=1060208211).

### Usuários e Acessos

Informações básicas de todos os usuários que utilizarão a solução, essenciais para a concessão automatizada de acessos:

- Nome de usuário;
- Empresa;
- E-mail;
- Grupo de acesso.

### Configurações Tributárias (ICMS)

Pacote de XMLs de NF-e, em formato .zip, contendo os arquivos XML dos últimos 6 meses (preferencialmente, dos últimos 12 meses).

 [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/26322304673943-Assistente-de-Melhores-Pr%C3%A1ticas#top)

## Configurações Iniciais

### Empresas

No menu Configurações Iniciais, selecione **"Empresas"** para iniciar o cadastro. Nesta etapa, será realizado o **"Cadastro de Empresas"** e o registro dos **"Certificados digitais"**.

![Imagem 3: No menu Configurações Iniciais , selecione "Empresas" para iniciar o cadastro. Nesta etapa, será realizado o "Cadastro…](https://ajuda.sankhya.com.br/hc/article_attachments/26972973777559)

#### Cadastro de Empresas

1. Clique em **"Iniciar"**. O sistema buscará automaticamente as empresas cadastradas e licenciadas.
2. Verifique os dados que serão utilizados para o cadastro e a instalação das melhores práticas.
3. Para concluir essa fase, clique em **"Instalar"** e aguarde a finalização do cadastro.

[GIF animado: Imagem 4: Para concluir essa fase, clique em "Instalar" e aguarde a finalização do cadastro.](https://ajuda.sankhya.com.br/hc/article_attachments/26976028473239)

Para avançar no processo de cadastro, selecione **"Continuar configurando"**. Caso queira continuar em outro momento, clique em **"Finalizar"**.

#### Certificados digitais

1. Selecione um certificado digital ativo.
2. Faça o upload do certificado no formato Modelo A1.
3. Digite a senha. Lembre-se de guardar esta senha em um local seguro.

[GIF animado: Imagem 5: Digite a senha. Lembre-se de guardar esta senha em um local seguro.](https://ajuda.sankhya.com.br/hc/article_attachments/26975101657111)

---

### Dados bancários

1. Clique em **"Cadastrar"** e preencha os campos conforme os dados da conta. Repita o processo para cada conta que deseja adicionar.
2. Indique se deseja ou não criar essa conta **"Tesouraria"** para as empresas registradas no ambiente.
3. Verifique todas as informações e clique em **"Instalar"**.

[GIF animado: Imagem 6: Verifique todas as informações e clique em "Instalar" .](https://ajuda.sankhya.com.br/hc/article_attachments/26970975820183)

---

### Parceiros

1. Baixe o [Modelo de Planilha](https://docs.google.com/spreadsheets/d/1wmUCOJFtsDYIcG2veMNiHmdZzTouf4s9tJfqlvDmrig/edit?gid=474794757#gid=474794757) para importar seus parceiros (Clientes, Fornecedores, entre outras).
2. Em seguida, faça o upload do arquivo (.xls ou .xlsx).
3. Revise a prévia dos itens importados.
4. Clique em **"Instalar"** para concluir essa etapa de configuração.

[GIF animado: Imagem 7: Clique em "Instalar" para concluir essa etapa de configuração.](https://ajuda.sankhya.com.br/hc/article_attachments/26971234231831)

---

### Produtos

1. Baixe o [Modelo de Planilha](https://docs.google.com/spreadsheets/d/1eQNfw_4JJaLHOtT1c4doR8-WlAsVs26EF4FZWSOTni4/edit?gid=531240979#gid=531240979) para importar seus produtos e vinculá-los à hierarquia de grupos de produtos.
2. Depois, faça o upload do arquivo (.xls ou .xlsx).
3. Verifique a pré-visualização dos itens importados.
4. Clique no botão **"Instalar"** para aplicar os dados e concluir a configuração.

[GIF animado: Imagem 8: Clique no botão "Instalar" para aplicar os dados e concluir a configuração.](https://ajuda.sankhya.com.br/hc/article_attachments/26976507892631)

---

### Usuários e acessos

1. Nesta etapa, o Sankhya sugerirá Grupos de Usuários predefinidos.
2. Visualize os **"Grupos de Usuário"** predefinidos e, se necessário, desative, edite ou adicione grupos conforme as necessidades do seu negócio.
3. Após isso, cadastre os **"Usuários"** no **Sankhya Om**, vinculando-os aos grupos criados.
4. Realize a conferência dos dados que serão cadastrados no ambiente e clique em **"Instalar"**.

[GIF animado: Imagem 9: Realize a conferência dos dados que serão cadastrados no ambiente e clique em "Instalar" .](https://ajuda.sankhya.com.br/hc/article_attachments/26972511226391)

 [[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/26322304673943-Assistente-de-Melhores-Pr%C3%A1ticas#top)

## Processos

Esta seção inclui várias rotinas do sistema, iniciando pela fase de compras. A seguir, são apresentadas as configurações essenciais para assegurar uma gestão eficiente das aquisições:

### Compras

#### Análise da necessidade e possibilidade de compra.

Para configurar a compra com base nos níveis de estoque mínimo e máximo utilizando relatórios, siga os passos abaixo:

1. Defina quais **"Usuários"** e/ou **"Grupos de Usuário"** irão realizar a análise dos relatórios relacionados à necessidade de compras.
2. Revise os Usuários ou Grupos de Usuário definidos.
3. Após essa verificação, clique em **"Instalar"** para ativar as configurações.

Para configurar a compra com base em pedidos de venda, realize as configurações abaixo:

1. Verifique se algum dos serviços listados pode ser utilizado para registrar Notas Fiscais de Energia Elétrica.
2. Analise se algum dos **"Grupos de Produtos/Serviços"** pode ser usado para cadastrar o Serviço de Energia Elétrica.
3. Identifique quais operações de entrada são realizadas pela empresa.
4. Determine quais **"Usuários"** são responsáveis pela análise dos relatórios de compras baseados em pedidos de venda.
5. Verifique as definições e, em seguida, clique em **"Instalar"** para aplicar as configurações.

---

#### Registro e histórico das compras

As configurações necessárias para o registro do pedido de compra incluem:

1. Defina quais dos **"Usuários"** e/ou **"Grupos de Usuário"** cadastrados serão responsáveis pelas compras da organização.
2. Indique se gostaria de registrar o comprador responsável nos pedidos.
3. Em seguida, revise as configurações realizadas e clique em **"Instalar"** para aplicá-las.

Para o envio de pedidos de compra por e-mail, realize as configurações abaixo:

1. Indique se utiliza o servidor de e-mails do Google.
   - Se sim, é necessário configurar as credenciais, incluindo **"Client ID"** e **"Client Secret"**.
   - Caso não, prossiga para o próximo passo.
2. Especifique se há contas de e-mail distintas para cada empresa no envio de mensagens pelo **Sankhya Om**.
3. Informe todas as contas SMTP que deseja configurar para o envio dos pedidos.
4. Verifique as informações fornecidas e clique em **"Instalar"** para aplicar a configuração.

Para o controle de pedidos de compra pendentes, siga as configurações abaixo:

1. Selecione quais **"Usuários"** e/ou **"Grupos de Usuário"** são responsáveis pelo controle dos Pedidos de Compras Pendentes.
2. Verifique as configurações definidas e clique em **"Instalar"**.

---

#### Registro das entradas, notas fiscais e devoluções

Configurações necessárias para compra para revenda e frete:

1. Marque quais **"Usuários"** e/ou **"Grupos de Usuário"** são responsáveis pelo lançamento das Notas de Compra e Conhecimentos de Transporte, garantindo a correta entrada de produtos no estoque.
2. Indique se algum dos **"Grupos de Produtos ou Serviços"** listados é adequado para o cadastro do Serviço de Transporte.
3. Informe os valores padrões para os campos necessários na importação de Conhecimentos de Transporte Eletrônico (CT-e).
4. Verifique as configurações realizadas e clique em **"Instalar"** para aplicá-las.

Para outras operações de entradas, efetue as configurações abaixo:

1. Indique se algum dos serviços listados pode ser utilizado para o registro de Notas Fiscais de Energia Elétrica.
2. Indique se algum dos **"Grupos de Produtos ou Serviços"** listados é apropriado para o cadastro do Serviço de Energia Elétrica.
3. Especifique quais das operações de entrada listadas são realizadas na empresa.
4. Informe quais usuários realizam o lançamento dessas Operações de Entrada.
5. Confira as informações fornecidas e clique em **"Instalar"** para aplicar as configurações.

Para o manifesto do destinatário de Nota Fiscal Eletrônica, realize as configurações abaixo:

1. Indique quais **"Usuários"** e/ou **"Grupos de Usuário"** são responsáveis pela manifestação de destinatário.
2. Em seguida, revise as definições e clique em **"Instalar"**.

Realize as configurações abaixo para efetuar a devolução de compras:

1. Determine quais **"Usuários"** e/ou **"Grupos de Usuário"** são responsáveis pelo lançamento dessas Operações de Entrada.
2. Depois, revise as informações fornecidas e clique em **"Instalar"** para aplicar as configurações.

---

![Imagem 10: A etapa de "Processos" abrange várias rotinas do sistema. Neste artigo, foi abordada apenas a fase de compras. É…](https://ajuda.sankhya.com.br/hc/article_attachments/27167139865111) A etapa de **"Processos"** abrange várias rotinas do sistema. Neste artigo, foi abordada apenas a fase de compras. É importante destacar que as orientações apresentadas se aplicam de maneira semelhante aos demais processos do sistema. Para conferir cada etapa e como configurá-la, basta seguir as instruções disponíveis em cada seção de configuração na tela.

---

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/26322304673943-Assistente-de-Melhores-Pr%C3%A1ticas#top)
