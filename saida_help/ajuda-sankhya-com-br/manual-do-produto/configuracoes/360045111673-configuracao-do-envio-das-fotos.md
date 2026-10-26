---
id: "360045111673"
titulo: "Configuração do Envio das Fotos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111673-Configura%C3%A7%C3%A3o-do-Envio-das-Fotos"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:58:10Z"
rotulos: ["Produtos", "manual", "Configuração", "Eventos", "Email", "FTP", "Álbum de Fotos", "Grupo de Produto", "Configuração do Envio das Fotos", "FTP das Fotos", "Aparência do Site", "Arquivo Modelo", "br.com.sankhya.mge.configuracaoenviofotos", "Configuração do Envio das Fotos manual", "Configuração do Envio de Fotos: Simplificando o Processo", "Fotos"]
---

# Configuração do Envio das Fotos

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310975059863) Módulo: Configurações > Avançado> Fotos de Eventos
```

---

Aqui você realiza as configurações de FTP, escolhe o grupo de produtos para álbuns, arquivos de customização do site de seleção de fotos, modelo de email e se sua empresa utilizará questionário ou não.

![Imagem 2: Aqui você realiza as configurações de FTP, escolhe o grupo de produtos para álbuns, arquivos de customização do site de…](https://ajuda.sankhya.com.br/hc/article_attachments/1500007207062)

Na seção **"FTP das fotos"**, é necessário que você informe o **"Usuário"** do FTP e a **"Senha"**, bem como o **"Endereço"** que é a Porta do FTP que conterá as fotos dos clientes. É possível que as fotos fiquem num FTP externo ou no próprio computador local, onde está executando o Sankhya Om. Para que fiquem no computador local, deve ser instalado um servidor de FTP no computador e definir uma pasta da máquina para ser utilizada pelo FTP. Após cadastrar as informações do FTP, é possível verificar se o FTP está levantado e se as informações digitadas estão corretas através do botão **"Testar FTP"**.

Na seção **"Aparência do site de fotos"** você poderá informar um endereço do [Repositório de Arquivos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596594-Reposit%C3%B3rio-de-Arquivos) para a logo do site e para o CSS externo do site; para isso, faça o upload dos arquivos pelo Repositório de Arquivos e informe nesses campos apenas o caminho de onde o arquivo se encontra no repositório. O arquivo de logomarca deverá ser exclusivamente no formato **".png"**, e o arquivo para CSS no formato **".css"**. Essa logo aparecerá no topo da tela de seleção de fotos.

Na seção **"Outras configurações"** temos os seguintes campos:

**Grupo de produto dos álbuns:** Quando informamos um produto álbum numa nota de venda, a maneira que o sistema utiliza para reconhecer o produto como um álbum é utilizando o Grupo de Produtos; para isso, é preciso criar um grupo de produtos e vincular todos os produtos que são álbuns a esse grupo; caso não faça, na tela de seleção de fotos os álbuns não estarão disponíveis.

**Grupo de produto dos posters:** Informe nesse campo o código do grupo que os produtos álbuns do tipo posters são vendidos, que funciona da mesma forma que o grupo do Álbum.

**Arquivo modelo de e-mail p/ envio das fotos:** Nesse campo você poderá informar um modelo de e-mail personalizado que será enviado para o cliente. Existe um botão para download do modelo padrão, esse modelo nada mais é que um arquivo em linguagem HTML e possui algumas variáveis que poderão ser utilizadas para customização, por exemplo:

**&codparc** **-** código do parceiro que está enviando o e-mail.

**&nomeparc** - nome do parceiro que está enviando o e-mail.

**&codprojeto** - código do projeto (código do evento).

**&nomeprojeto** - identificação do projeto (identificação do evento).

**&razsoc** - razão social da empresa.

**&emaile** - e-mail da empresa.

**&datasis** - data do sistema (no momento do envio do e-mail).

**&horasis** - hora do sistema (no momento do envio do e-mail).

**&codacesso** - código do acesso para o parceiro acessar o link de edição.

**&link\_edicao** - link de edição das fotos.

**&link\_votacao** - link de votação das fotos.

**Nota:** é recomendado que seja utilizado o modelo padrão como base para sua personalização.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111673-Configura%C3%A7%C3%A3o-do-Envio-das-Fotos#top)

![Imagem 3: Acesse também:](https://ajuda.sankhya.com.br/hc/article_attachments/16516325825431) Acesse também:

[Manual de Implantação e Utilização do Álbum de Fotos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602074-Manual-de-Implanta%C3%A7%C3%A3o-e-Utiliza%C3%A7%C3%A3o-de-%C3%81lbum-de-Fotos)
