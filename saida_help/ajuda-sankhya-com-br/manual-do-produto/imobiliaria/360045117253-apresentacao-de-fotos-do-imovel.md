---
id: "360045117253"
titulo: "Apresentação de Fotos do Imóvel"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045117253-Apresenta%C3%A7%C3%A3o-de-Fotos-do-Im%C3%B3vel"
trilha: "Manual do Produto > Imobiliária > Imobiliária"
atualizado_em: "2026-07-29T14:08:37Z"
rotulos: ["Configuração", "FTP", "br.com.sankhya.tim.cad.timtimfotosimovelh5", "Configuração de parâmetros", "Acesso externo às imagens", "Visualização de fotos", "Imobiliária", "Prospecção", "WGE"]
---

# Apresentação de Fotos do Imóvel

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42311361348247) Módulo: Imobiliária > Rotinas > Prospecção
![Imagem 2](https://ajuda.sankhya.com.br/hc/article_attachments/42311361349655) Versão disponível: a partir da 3.31
```

---

Esta rotina exibirá as fotos que foram vinculadas à um determinado imóvel através da tela [Imóveis](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608914), botão **"Ações..."**, opção **"Enviar Fotos"**.

![Imagem 3: Esta rotina exibirá as fotos que foram vinculadas à um determinado imóvel através da tela Imóveis , botão "Ações..." ,…](https://ajuda.sankhya.com.br/hc/article_attachments/360061017094)

**Observação:** esta tela será aberta automaticamente, quando na rotina de Cadastro de Imóveis, a opção **"Ver Fotos"** do botão Ações... for selecionada.

**Importante:** as fotos apenas serão apresentadas nesta tela se na configuração dos parâmetros **"Caminho do FTP para a pasta de fotos dos imóveis - TIMFTPFOTIMOV"** e **"Path relativo do repositório para fotos do Imóvel - TIMPATHREPIMOV"**constar o mesmo caminho do Repositório de Arquivos onde foram salvas as imagens. Além disso, é necessário preencher o parâmetro **"Endereço para acesso externo ao WGE- ENDACESSEXTWGE"**, para que o sistema acesse as imagens definidas para o imóvel selecionado, com a seguinte formatação: http://[ip-externo]:[porta]/timimob/integracao/downloadfotos/?imovel=[cod-imovel]&foto=nomeImagem.jpg.
