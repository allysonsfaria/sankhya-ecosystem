---
id: "30450376137879"
titulo: "Importação de Cupom Fiscal com Registro Automático de Abastecimento"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/30450376137879-Importa%C3%A7%C3%A3o-de-Cupom-Fiscal-com-Registro-Autom%C3%A1tico-de-Abastecimento"
trilha: "Sankhya Official Pack - SOP > Frotas"
atualizado_em: "2026-07-22T14:35:51Z"
rotulos: ["Configuração", "XML", "Importação", "TOP", "br.com.sankhya.core.cad.veiculos", "Financeiro", "Importação de Cupom Fiscal com Registro Automático de Abastecimento", "registro automático de abastecimento", "br.com.sankhya.soplogistica.cad.abastecimento", "cupom fiscal", "automatizar registro de abastecimento", "Abastecimento"]
---

# Importação de Cupom Fiscal com Registro Automático de Abastecimento

#### 1. Configurações:

Para automatizar o registo de abastecimento ao importar um cupom fiscal, siga os passos abaixo:

![Imagem 1: Acesse o cadastro da TOP de compra;](https://ajuda.sankhya.com.br/hc/article_attachments/30450582868119)  Acesse o cadastro da TOP de compra;

![Imagem 2: Marque as seguintes opções:](https://ajuda.sankhya.com.br/hc/article_attachments/30450570769815) Marque as seguintes opções:

- Importar Motorista da Observação
- Importar Veículo da Observação
- Importar KM da Observação
- Gerar abastecimento na confirmação

#### 2. Como funciona:

Ao importar o XML do cupom fiscal no portal de compras e confirmar a nota, o sistema irá:

- Criar automaticamente um registro de abastecimento na tela **"Lançamentos de abastecimento".**
- Atualizar o Histórico de KM do veículo com base nas informações do cupom fiscal.

**Observação:**
Certifique-se de que as informações de motorista, veículo e quilometragem estejam presentes na observação do cupom fiscal para que o processo funcione corretamente.

**Evidencias:**
Importado o xml, os campos de motorista, veículo e km serão preenchidos automaticamente, pegando a informação da observação do xml.

![Imagem 3: Evidencias: Importado o xml, os campos de motorista, veículo e km serão preenchidos automaticamente, pegando a…](https://ajuda.sankhya.com.br/hc/article_attachments/30450582872983)

Ao confirmar a nota na central de compras, foi gerado automaticamente os registros na tela Lançamentos de abastecimentos. Sendo gerada uma linha para cada produto do tipo combustível.

![Imagem 4: Ao confirmar a nota na central de compras, foi gerado automaticamente os registros na tela Lançamentos de…](https://ajuda.sankhya.com.br/hc/article_attachments/30453716180119)

![Imagem 5: Ao confirmar a nota na central de compras, foi gerado automaticamente os registros na tela Lançamentos de…](https://ajuda.sankhya.com.br/hc/article_attachments/30453729226007)

O registro será gerado também na aba de histórico de Km no cadastro do veículo.

![Imagem 6: O registro será gerado também na aba de histórico de Km no cadastro do veículo.](https://ajuda.sankhya.com.br/hc/article_attachments/30453729226903)
