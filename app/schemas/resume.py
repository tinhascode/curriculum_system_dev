from pydantic import BaseModel, ConfigDict, EmailStr, Field


class Experience(BaseModel):
    model_config = ConfigDict(extra="forbid")

    cargo: str = Field(..., max_length=120, description="Cargo ou posição exercida")
    empresa: str = Field(..., max_length=120, description="Nome da empresa")
    periodo: str = Field(
        ..., max_length=60, description="Período de atuação (ex: Jan 2022 - Atual)"
    )
    realizacoes: list[str] = Field(
        default_factory=list,
        max_length=10,
        description="Lista de realizações ou responsabilidades",
    )


class Education(BaseModel):
    model_config = ConfigDict(extra="forbid")

    curso: str = Field(..., max_length=150, description="Nome do curso ou graduação")
    instituicao: str = Field(
        ..., max_length=150, description="Nome da instituição de ensino"
    )
    periodo: str = Field(
        ..., max_length=60, description="Período de realização (ex: 2018 - 2022)"
    )


class Resume(BaseModel):
    model_config = ConfigDict(extra="forbid")

    nome: str = Field(..., max_length=120, description="Nome completo")
    cargo: str = Field(..., max_length=120, description="Cargo ou título desejado")
    email: EmailStr = Field(..., description="E-mail de contato")
    telefone: str = Field(..., max_length=30, description="Telefone de contato")
    cidade: str = Field(
        default="", max_length=80, description="Cidade e Estado (ex: São Paulo, SP)"
    )
    link: str = Field(
        default="",
        max_length=200,
        description="Link profissional (ex: LinkedIn ou GitHub)",
    )
    resumo: str = Field(
        default="",
        max_length=800,
        description="Resumo profissional com foco em resultados",
    )
    experiencias: list[Experience] = Field(
        default_factory=list,
        max_length=10,
        description="Histórico profissional (até 10)",
    )
    formacao: list[Education] = Field(
        default_factory=list,
        max_length=6,
        description="Formação acadêmica (até 6)",
    )
    habilidades: list[str] = Field(
        default_factory=list,
        max_length=40,
        description="Habilidades técnicas e comportamentais (até 40)",
    )
    idiomas_certificacoes: list[str] = Field(
        default_factory=list,
        max_length=15,
        description="Idiomas e certificações relevantes (até 15)",
    )
