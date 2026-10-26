---
id: "37886668069143"
titulo: "Como realizar a conferência do Certificado Digital"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37886668069143-Como-realizar-a-confer%C3%AAncia-do-Certificado-Digital"
trilha: "Universidade Sankhya > Jornada de Cadastros Globais"
atualizado_em: "2026-07-22T14:05:37Z"
rotulos: ["Configuração", "NF-e", "SEFAZ", "Certificado Digital", "Documentos Eletrônicos"]
---

# Como realizar a conferência do Certificado Digital

## O que é o certificado digital?

O Certificado Digital é essencial para a emissão de documentos fiscais eletrônicos. O sistema Sankhya utiliza o modelo A1 para certificação digital, sendo necessário realizar a importação e configuração adequada para seu funcionamento.

#### Vídeo de demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/845085006)

#### Siga o passo a passo para incluir o certificado digital em sua base

1. Acesse a tela **Console NFe**

**Menu:** Comercial » Configuração » Console NFe

**Aba Registro de Certificado**

- Clique em "**+ Inserir Registro**".
- No campo **Certificado**, clique em "**Procurar**" e selecione o certificado digital da empresa.
- Preencha os demais campos obrigatórios (como empresa, validade, entre outros).
- Clique em "**Salvar registro"** para concluir o processo.

**Aba Status do Serviço**

- Esta aba serve para verificar se os serviços fiscais estão funcionando corretamente (NF-e, NFS-e, NFC-e, CT-e, MDF-e).
- Selecione o **CNPJ** da empresa.
- Escolha o **Estado** onde a empresa está localizada.
- Selecione o **Ambiente**:

**Produção** (notas válidas)

**Homologação** (ambiente de testes)

- Clique em **Testar**
- O sistema exibirá o status de disponibilidade dos serviços fiscais consultados.

**Aba Administração**

- Aqui são exibidos os logs de funcionamento do console, úteis para diagnóstico de erros.
- Você pode usar os botões:

**"Baixar Log"** – salva o log no computador

**"Recarregar Log"** – atualiza os dados exibidos

**"Limpar Log"** – remove os registros listados

**"Importação/Exportação"** – para transferir configurações entre ambientes

**Aba Configurações**

- Nesta aba, você pode ajustar parâmetros técnicos do funcionamento do SanNFe.
- Algumas configurações mais avançadas devem ser feitas diretamente no arquivo san-nfe.conf, localizado na pasta conf do diretório onde o SanNFe foi instalado.
- Essas configurações ajudam a melhorar o desempenho do envio de notas fiscais eletrônicas.
