---
id: "5127428683031"
titulo: "Configurações necessárias para lançar uma ocorrência de Licença Cárcere/Pessoal G"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/5127428683031-Configura%C3%A7%C3%B5es-necess%C3%A1rias-para-lan%C3%A7ar-uma-ocorr%C3%AAncia-de-Licen%C3%A7a-C%C3%A1rcere-Pessoal-G"
trilha: "Dúvidas Frequentes > MGE Folha"
atualizado_em: "2026-07-29T13:36:42Z"
rotulos: ["Configuração", "Funcionários", "Contrato", "Ocorrências", "Folha", "#Licençacarcere", "#pessoalg", "Lançamentos > Histórico do Funcionário > Histórico de Ocorrências", "Paralisação temporária sem salário sem contagem de tempo", "Cadastro afastamento fórmula cálculo proporcional"]
---

# Configurações necessárias para lançar uma ocorrência de Licença Cárcere/Pessoal G

Em algumas situações tem-se a ‘Suspensão do contrato de trabalho’ que seria a paralisação temporária dos serviços, sendo que o empregado não recebe salário e não existe contagem de tempo de serviço. Isto ocorre quando o funcionário é preso e, assim, permanece um período afastado do trabalho, que pode durar até seu julgamento ou prazos determinados pela Legislação Penal. A previsão para esse afastamento temporário encontra-se no artigo 131, inciso V, da CLT.

### Configurações necessárias:

![Imagem 1: Cadastro da ocorrência](https://ajuda.sankhya.com.br/hc/article_attachments/16348505576343) Cadastro da ocorrência

Acesse a tela: Lançamentos > Histórico do Funcionário > Histórico de Ocorrências… :

![Imagem 2: Acesse a tela: Lançamentos > Histórico do Funcionário > Histórico de Ocorrências… :](https://ajuda.sankhya.com.br/hc/article_attachments/15776092870551)

![Imagem 3: Acesse a tela: Lançamentos > Histórico do Funcionário > Histórico de Ocorrências… :](https://ajuda.sankhya.com.br/hc/article_attachments/5127040787863)

![Imagem 4: Cadastre o evento](https://ajuda.sankhya.com.br/hc/article_attachments/16348505581463) Cadastre o evento

Acesse a tela: Arquivos > Eventos

![Imagem 5: Acesse a tela: Arquivos > Eventos](https://ajuda.sankhya.com.br/hc/article_attachments/5127085279383)

![Imagem 6: Acesse a tela: Arquivos > Eventos](https://ajuda.sankhya.com.br/hc/article_attachments/5127063979159)

![Imagem 7: Acesse a tela: Arquivos > Eventos](https://ajuda.sankhya.com.br/hc/article_attachments/5127065386775)

![Imagem 8: Acesse a tela: Arquivos > Eventos](https://ajuda.sankhya.com.br/hc/article_attachments/5127101146263)

| **Fórmula:**   (&F1007 / &DiaDivSalBase) \* FDiasAfaMotivo(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&REFERE,'2',&TIPFOL)  Índice: FDiasAfaMotivo(QueFuncionario.CODEMP,QueFuncionario.CODFUNC,&REFERE,'2',&TIPFOL) |
| --- |

Lembrando que se deve ter a fórmula auxiliar 1007 cadastrada, para que o cálculo seja realizado corretamente.

![Imagem 9: Registro da ocorrência](https://ajuda.sankhya.com.br/hc/article_attachments/16348505587479) Registro da ocorrência

Acesse a tela: Lançamentos> Histórico Colaboradores> Registros de Ocorrências…

![Imagem 10: Acesse a tela: Lançamentos> Histórico Colaboradores> Registros de Ocorrências…](https://ajuda.sankhya.com.br/hc/article_attachments/15776168590103)

Selecione a empresa e o empregado:

![Imagem 11: Selecione a empresa e o empregado:](https://ajuda.sankhya.com.br/hc/article_attachments/5127276777239)

Clique em “+” e realize o cadastro do afastamento:

![Imagem 12: Clique em “+” e realize o cadastro do afastamento:](https://ajuda.sankhya.com.br/hc/article_attachments/5127255681943)

![Imagem 13: Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/16348505588887) Cálculo

![Imagem 14: Cálculo](https://ajuda.sankhya.com.br/hc/article_attachments/5127250312471)

Se o funcionário trabalhar uma parte do mês e for afastado no restante, na folha deverá ser pago proporcional.
