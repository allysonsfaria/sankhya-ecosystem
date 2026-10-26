---
id: "360044349613"
titulo: "Falha ao conectar-se ao servidor de autorização de documentos eletrônicos. Tempo máximo excedido (Timeout)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044349613-Falha-ao-conectar-se-ao-servidor-de-autoriza%C3%A7%C3%A3o-de-documentos-eletr%C3%B4nicos-Tempo-m%C3%A1ximo-excedido-Timeout"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:58:08Z"
rotulos: ["Configuração", "NF-e", "Portal de Vendas", "SEFAZ", "CORE_E04183", "Erro de Conexão com SEFAZ ou SCAN", "Erro", "Documentos Eletrônicos"]
---

# Falha ao conectar-se ao servidor de autorização de documentos eletrônicos. Tempo máximo excedido (Timeout)

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/17086268022551) MENSAGEM:**

[CORE\_E04183] Falha ao conectar-se ao servidor de autorização de documentos eletrônicos. Tempo máximo excedido (Timeout).

**![Imagem 2: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17086282720407) SITUAÇÃO:**

Ao realizar emissão de NF-e pelo Portal de Vendas, no Sankhya W, apresenta a mensagem.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/17086268033431) CAUSA:**

Esta mensagem indica que ao gerar o lote não foi possível a comunicação com a SEFAZ (Secretaria da Fazenda). Isso pode ocorrer quando o servidor (computador em que está instalado o sistema) não está com acesso à internet, por regras de proxy que foram criadas recentemente ou, ainda, quando a SEFAZ da sua região está indisponível/instável.

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17086268031255) SOLUÇÃO:**

(1)** Servidor sem acesso à internet:**

Solicite apoio do profissional de TI da empresa para restabelecer a conexão do servidor com a internet. Assim que o problema for corrigido, realize a geração do lote novamente.

(1)** Verificar o Provedor do Cliente:**Verifique junto ao provedor que o Cliente utiliza, se aconteceu alguma mudança na estrutura do mesmo, como por exemplo se houve troca de IP de acesso. Neste caso, acione a equipe de TI da empresa para que seja realizado os devidos ajustes.

(1)** Regras de Proxy bloqueando acesso à SEFAZ:**

Algumas regras podem ser estabelecidas para restringir o acesso a determinados sites usando proxy. Se na sua empresa o proxy é utilizado, ele pode estar bloqueando o acesso à SEFAZ. Entre em contato com o seu suporte de TI para confirmar se sua rede possui esse tipo de regra configurada.

(1)** SEFAZ indisponível/instável:**

Para confirmar se a SEFAZ de seu estado está indisponível, consulte [clicando aqui](http://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx?versao=0.00&tipoConteudo=Skeuqr8PQBY=).

Estando indisponível, aguarde a normalização. Dependendo da necessidade, pode ser emitido notas em contingência. Para este processo recomendamos que leia o artigo “[Como configurar o envio de NF-e em contingência?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044294473)”, verificando se existem as parametrizações necessárias para emissão.

**(1)** **Certificado Digital:**Verifique se o certificado inserido se trata do original ou do backup.

Pois o certificado só pode ser instalado em apenas uma máquina, se for inserido o backup no console, o mesmo não irá comunicar e irá apresentar a mensagem de erro acima.
