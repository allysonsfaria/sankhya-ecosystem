---
id: "360044599654"
titulo: "CT-e Globalizado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044599654-CT-e-Globalizado"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-09-29T14:10:35Z"
rotulos: ["CT-e", "CT-e Globalizado", "Configuração", "CT-e Globalizado manual", "XML", "SEFAZ", "Transporte", "CT-e Globalizado: Simplificação Logística", "Transporte Eletrônico", "Documentos Eletrônicos"]
---

# CT-e Globalizado

O CT-e globalizado é um [Conhecimento de Transporte Eletrônico](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596834-Conhecimento-de-Transporte-Eletr%C3%B4nico-CT-e) que tem como premissa a origem e destino na mesma Unidade Federativa. Ele acoberta uma operação em que, quando o tomador do serviço é o remetente e são feitas várias entregas para vários destinatários e todas coletadas no remetente; já quando o destinatário é o tomador, são realizadas várias coletas para apenas uma entrega no destinatário. A grande vantagem do CT-e globalizado é evitar a emissão de vários documentos de CT-e para uma operação que pode ser acobertada pela emissão de um só documento.

Será possível identificar que um CT-e é globalizado por meio do campo **"CT-e Globalizado"** que pode ser incluído no cabeçalho do documento, por meio da tela [Configurador de Layout da Nota](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602634-Configurador-de-Layout-da-Nota). Uma vez identificado um CT-e globalizado, o Sankhya-OM conta com algumas regras de validação que irão implicar na confirmação e transmissão do CT-e para SEFAZ, são elas:

- A UF de origem e destino do CT-e deve ser obrigatoriamente a mesma;
- O tomador do serviço do CT-e deve ser ou o remetente ou o destinatário somente;
- Somente documentos de NF-e (modelo 55) podem fazer parte do CT-e;
- Se o tomador for o remetente, o destinatário deverá ser igual ao emitente;
- Se o tomador for o destinatário, o remetente deve ser igual ao emitente;
- Se o tomador for o remetente, todas os documentos de NF-e devem ser obrigatoriamente do mesmo emitente;
- Se o tomador for o destinatário, é preciso que existam ao menos 5 (cinco) emitentes diferentes entre os documentos de NF-e vinculados no CT-e.

Todas as regras de validação descritas acima, são aplicáveis somente se o CT-e for identificado como globalizado. No momento da sua confirmação ou transmissão/geração do lote, para cada regra de validação, em caso de discordância nas configurações, o sistema exibe uma mensagem esclarecendo o ajuste a ser realizado:

**"CT-e globalizado deve ter a origem e destino na mesma UF."**

**"Para emitir um CT-e globalizado o tomador deve ser o remetente ou o destinatário."**

**"Somente documentos de NF-e (modelo 55) podem fazer parte do CT-e globalizado."**

**"No CT-e globalizado quando o tomador é o remetente, o destinatário precisa ser o emitente."**

**"No CT-e globalizado quando o tomador é o remetente, todas as notas precisam ser do mesmo emitente."**

**"No CT-e globalizado quando o tomador é o destinatário, o remetente precisa ser o emitente."**

**"No CT-e globalizado quando o tomador é o destinatário, deve haver ao menos 5 emitentes diferentes."**

---

### XML CT-e Globalizado

Na geração do XML de um CT-e identificado como globalizado, serão consideradas as seguintes regras de negócios:

- Se o tomador do serviço for destinatário, o campo **"rem/xNome"** no XML será gerado igual a **"Diversos"**;
- Caso o tomador do serviço seja remetente, então o campo **"dest/xNome"** no XML será gerado igual a Diversos.

---

### Importação de NF-e para CT-e Globalizado

Em relação ao processo de importação de NF-e para emissão de CT-e, se o CT-e a ser gerado for globalizado, tem-se as seguintes validações:

- Devem ser vinculadas ao menos duas NF-e;
- Todas as NF-e's vinculadas devem possuir um mesmo remetente (emitente da nota) com diferentes destinatários, ou um mesmo destinatário, com pelo menos cinco remetentes (emitente da nota) diferentes entre si.

Caso alguma das condições acima não seja atendida, será exibida uma mensagem informando o motivo da não geração do CT-e.
