---
id: "44010353010583"
titulo: "Como receber leads na Meetime utilizando o Make"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010353010583-Como-receber-leads-na-Meetime-utilizando-o-Make"
trilha: "Meetime > Integrações"
atualizado_em: "2026-10-05T18:37:01Z"
rotulos: ["sync_hc", "meetime", "sync_hash_ff55d7b79565", "meetime_335"]
---

# Como receber leads na Meetime utilizando o Make

Make é uma ferramenta de automação que conecta sistemas e executa fluxos automáticos. Para usar essa ação, basta ter uma conta no Make e uma conta na Meetime com perfil de administrador ou gestor. Com isso configurado, o Make consegue receber ou enviar dados e executar o fluxo conforme os eventos definidos.

Existem duas formas de receber leads na Meetime usando o Make, e isso depende do tipo de campo que você quer integrar. A primeira forma serve para quem quer integrar apenas os campos padrão da Meetime. Já a segunda é para quem precisa integrar usando campos personalizados.

## Envio de Campos Padrão

1. Antes de tudo, será necessário que você possua uma conta no [Make](https://www.make.com/en). Já no sistema, você deverá clicar no menu “**Scenarios” > Create a new scenario** (nome dado para o ambiente onde integrações são construídas por lá).

![Imagem 1: Antes de tudo, será necessário que você possua uma conta no Make . Já no sistema, você deverá clicar no menu “…](https://ajuda.sankhya.com.br/hc/article_attachments/44010378663319)

1. Na etapa inicial, você deverá selecionar a **ferramenta de onde os leads serão disparados** (por exemplo Active Campaign, Pipedrive, uma planilha do Google Sheets, entre outros).

![Imagem 2: Na etapa inicial, você deverá selecionar a ferramenta de onde os leads serão disparados (por exemplo Active Campaign,…](https://ajuda.sankhya.com.br/hc/article_attachments/44010395716887)

1. Depois, basta clicar para adicionar outro módulo > pesquisar pela **Meetime > Create a Prospect**:

![Imagem 3: Depois, basta clicar para adicionar outro módulo > pesquisar pela Meetime > Create a Prospect :](https://ajuda.sankhya.com.br/hc/article_attachments/44010344262679)

1. Será necessário dar sequência integrando a conta da Meetime que você desejará utilizar em **“Connection”** através da **API Key** que fica disponível para usuários **Gestores e Administradores** na tela da Meetime (link [aqui](https://meetime.com.br/dashboard/integrations/api)).

Obs.: caso a chave/token de API não apareça na sua tela, basta solicitar a habilitação ao nosso Suporte através do e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br).

![Imagem 4: Obs.: caso a chave/token de API não apareça na sua tela, basta solicitar a habilitação ao nosso Suporte através do…](https://ajuda.sankhya.com.br/hc/article_attachments/44010404744599)

1. Nos campos seguintes, os parâmetros da entrada do lead na Meetime devem ser mapeados:
2. Em qual **cadência** ele deve entrar;
3. Se já deve iniciar imediatamente ao ser criado no nosso sistema - o que já disponibiliza as atividades para o SDR realizar (campo “**Start Immediately**”);
4. Informações como e-mail, nome completo, empresa, etc. (que podem ser preenchidos com o que vier do sistema que disparará os leads - o Make permite fazer essa **associação**).

![Imagem 5: Informações como e-mail, nome completo, empresa, etc. (que podem ser preenchidos com o que vier do sistema que…](https://ajuda.sankhya.com.br/hc/article_attachments/44010396759575)

Para **testar** a funcionalidade, basta clicar em "**executar**":

![Imagem 6: Para testar a funcionalidade, basta clicar em " executar ":](https://ajuda.sankhya.com.br/hc/article_attachments/44010405458071)

## Envio de Campos Personalizados

Atualmente, não é possível preencher **campos personalizados** na Meetime com o formato padrão do Make (descrito anteriormente neste artigo).

Caso você deseje enviá-los para nosso sistema, será necessário utilizar outro formato oferecido pelo Make, após buscar pelo sistema da Meetime, chamado “**Make an API Call**” (que permite adicionar os campos personalizados diretamente no corpo da requisição):

![Imagem 7: Caso você deseje enviá-los para nosso sistema, será necessário utilizar outro formato oferecido pelo Make, após buscar…](https://ajuda.sankhya.com.br/hc/article_attachments/44010381233175)

Campo **“URL”** e Campo “**Method**”

1° É necessário preencher o endereço da cadência para disparo via API: usuários Gestores ou Administradores conseguem pegá-lo entrando na **Meetime > menu Prospecção > Cadências** > nome da cadência desejada > “Envio de leads via integração” no rodapé da página > Ícone para copiar o link de API.

**Ponto importante:** Utilizar URL a patir de /v2: dessa forma --> /v2/prospections/cadence/58818/lead...

2° Selecionar “**POST**” (pois é o método para criar algo em um sistema)

**Na Meetime:**

![Imagem 8: Na Meetime:](https://ajuda.sankhya.com.br/hc/article_attachments/44010397686295)

**No Make:**

![Imagem 9: No Make:](https://ajuda.sankhya.com.br/hc/article_attachments/44010432126999)

Campo “**Body**”

Preencher o corpo da requisição; é possível verificar um modelo da estrutura que deve ser colocada no Body na documentação da **API da Meetime**, basta clicar [aqui](https://meetime.readme.io/reference/adicionarleadsnameetimeiniciarumanovaprospecoolead) e preencher os campos que aparecem no centro da página e copiar o que aparecerá no lado direito da tela (fundo preto):

Obs.: esses campos podem ser preenchidos com qualquer informação pois posteriormente devem ser trocadas no Make; por exemplo: no GIF o cargo está preenchido com “Diretor”, mas no Make será necessário substituir essa palavra pelo campo na ferramenta inicial (que fará o disparo dos leads) que corresponde ao cargo (e que varia de lead para lead).

**Na API:**

![Imagem 10: Na API:](https://ajuda.sankhya.com.br/hc/article_attachments/44010406859159)

**No Make:**

![Imagem 11: No Make:](https://ajuda.sankhya.com.br/hc/article_attachments/44010382489495)

Obs. 2: os campos personalizados que aparecem na documentação da API são apenas exemplos, porém eles ajudam a verificar como deve ser o preenchimento do corpo da requisição, basta apenas verificar o nome interno dos campos personalizados da sua conta para substituir os nomes desses campos (esse nome interno pode ser visto por usuários Gestores e Administradores na Meetime, basta clicar no menu Prospecção > Ajustes > Campos dos Leads > Ícone de três pontinhos ao lado direito > Copiar chave de API).

**Ponto de atenção**

Para preencher **campos personalizados** do tipo **“campo de seleção”** na Meetime, é necessário enviar, via Make, o ID da opção a preenchê-lo e não o texto.

Vamos a um exemplo: tenho o campo personalizado “Funcionários” dentro da Meetime e algumas opções para preenchê-lo: opção 1 sendo "51-100", opção 2 sendo "Mais de 100" e assim por diante. Se desejo preencher esse campo via Make, devo colocar, após o título do campo, a opção da seguinte forma:

![Identificador de cada opção de um campo de seleção (PICKLIST)](https://ajuda.sankhya.com.br/hc/article_attachments/44010398718231)

Esses valores internos podem ser buscados ou via API (link da documentação [aqui](https://meetime.readme.io/reference/listarcampospersonalizados)) ou na própria tela da Meetime, basta que um usuário Gestor ou Administrador clique no menu **Prospecção > Campos dos Leads > Título do campo > Ícone de chave ao lado de cada opção**.

Para criar uma tabela de comparação no Make, para que ele possa enviar o valor “xyz1” para preencher o campo “Segmento” na Meetime quando a opção vinda da ferramenta inicial é “Indústria”, você pode utilizar a funcionalidade de Data Store do próprio Make (mais informações [aqui](https://www.make.com/en/help/tools/data-store?_gl=1*12n3u2z*_gcl_au*MTg0MTg4NzIwLjE3Mzc1NDkxMTU.*_ga*MTMzOTYyMDk3NS4xNzIzNjQyMTc5*_ga_MY0CJTCDSF*MTczNzY1ODYwMi45LjEuMTczNzY1OTAyMy4yNS4wLjA.)).

---

Ainda tem dúvidas? Entre em contato com a gente através do 
e-mail [suporte@meetime.com.br](mailto:suporte@meetime.com.br) ou WhatsApp através do número de telefone [(48) 3204-7590](https://wa.me/554832047590).
