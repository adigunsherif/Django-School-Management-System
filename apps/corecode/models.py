from django.urls import reverse
from django.utils import timezone
from django.db import models

# Create your models here.


class SiteConfig(models.Model):
    """Site Configurations"""

    key = models.SlugField()
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.key


class PermitDocCategory(models.Model):
    """DocumentCategory"""

    name = models.CharField(max_length=200, unique=True)

    class Meta:
        #verbose_name = "Наименование"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Citizenship(models.Model):
    """Citizenship"""

    name = models.CharField(max_length=100)

    class Meta:
        #verbose_name = "Наименование"
        ordering = ["name"]

    def __str__(self):
        return self.name
        

class AcademicSession(models.Model):
    """Academic Session"""

    name = models.CharField(max_length=200, unique=True)
    current = models.BooleanField(default=True)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name


class AcademicTerm(models.Model):
    """Academic Term"""

    name = models.CharField(max_length=20, unique=True)
    current = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Subject(models.Model):
    """Subject"""

    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class StudentClass(models.Model):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
        ordering = ["name"]

    def __str__(self):
        return self.name

class DocumentType(models.Model):
    """DocumentType"""

    name = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class Gen_DT_DocumentType(models.Model):
    """Gen_DT_DocumentType"""

    DocumentTypeEN = models.CharField(max_length=200)
    DocumentTypeRU = models.CharField(max_length=200)
    DocumentTypeTR = models.CharField(max_length=200)

    class Meta:
        ordering = ["DocumentTypeEN"]

    def __str__(self):
        return self.DocumentTypeEN
    
class Gen_DT_Country(models.Model):
    """Gen_DT_Country"""

    CountryCode = models.CharField(max_length=50, unique=True)
    CountryEN = models.CharField(max_length=100)
    CountryRU = models.CharField(max_length=100)
    CountryTR = models.CharField(max_length=100)
    AlphaCode2 = models.CharField(max_length=10, verbose_name="AlphaCode(2)")
    AlphaCode3 = models.CharField(max_length=10, verbose_name="AlphaCode(3)")
    CountriesForRF = models.BooleanField(default=False)
    LocalEEC = models.BooleanField(default=False, verbose_name="Local/ EEC")
    RvpVnj = models.BooleanField(default=False, verbose_name="RVP/ VNJ")
    Visa = models.BooleanField(default=False)
    VKS = models.BooleanField(default=False)
    Patent = models.BooleanField(default=False)

    class Meta:
        #verbose_name =CountryEN "Наименование"
        ordering = ["CountryEN"]

    def __str__(self):
        return self.CountryEN
    
class Gen_DT_Discipline(models.Model):
    """Gen_DT_Discipline"""

    DisciplineEN = models.CharField(max_length=200)
    DisciplineRU = models.CharField(max_length=200)
    DisciplineTR = models.CharField(max_length=200)

    class Meta:
        ordering = ["DisciplineEN"]

    def __str__(self):
        return self.DisciplineEN
    
    
class Gen_DT_EmpLevel(models.Model):
    """Gen_DT_EmpLevel"""

    EmpLevelEN = models.CharField(max_length=200)
    EmpLevelRU = models.CharField(max_length=200)
    EmpLevelTR = models.CharField(max_length=200)
    OfficeEmp = models.BooleanField(default=False)
    ProjectEmp = models.BooleanField(default=True)

    class Meta:
        ordering = ["EmpLevelEN"]

    def __str__(self):
        return self.EmpLevelEN
    
    
class Gen_DT_EmpClass(models.Model):
    """Gen_DT_EmpClass"""

    EmpClassEN = models.CharField(max_length=200)
    EmpClassRU = models.CharField(max_length=200)
    EmpClassTR = models.CharField(max_length=200)

    class Meta:
        ordering = ["EmpClassEN"]

    def __str__(self):
        return self.EmpClassEN
    
class Gen_DT_JobTitle(models.Model):
    """Gen_DT_JobTitle"""

    JobTitleEN = models.CharField(max_length=200)
    JobTitleRU = models.CharField(max_length=200)
    JobTitleTR = models.CharField(max_length=200)

    EmpLevel = models.ForeignKey(
        Gen_DT_EmpLevel, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee Level"
    )

    EmpClass = models.ForeignKey(
        Gen_DT_EmpClass, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee Class"
    )

    class Meta:
        ordering = ["JobTitleEN"]

    def __str__(self):
        return self.JobTitleEN
    
class Gen_DT_Currency(models.Model):
    """Gen_DT_Currency"""

    CurrencyNumber = models.IntegerField(unique=True)
    CurrencyID_1C = models.CharField(max_length=100)
    CurrencyCode = models.CharField(max_length=100)
    CountryAlphaCode2 = models.CharField(max_length=10, verbose_name="AlphaCode(2)")
    CountryAlphaCode3 = models.CharField(max_length=10, verbose_name="AlphaCode(3)")
    CurrencyEN = models.CharField(max_length=200)
    CurrencyRU = models.CharField(max_length=200)
    CurrencyTR = models.CharField(max_length=200)
    ActiveCurr = models.BooleanField(default=False)

    class Meta:
        ordering = ["CurrencyNumber"]

    def __str__(self):
        return self.CurrencyNumber
    
class Gen_DT_CBR_Rates(models.Model):
    """Gen_DT_CBR_Rates"""

    DateCBR = models.DateField()
    RateUSD = models.CharField(max_length=200)
    RateEUR = models.CharField(max_length=200)

    class Meta:
        ordering = ["RateEUR"]

    def __str__(self):
        return self.RateEUR
    
class Gen_DT_CounterParty(models.Model):
    """Gen_DT_CounterParty"""

    CounterPartyID_1C = models.CharField(max_length=100)
    CounterPartyEN = models.CharField(max_length=200)
    CounterPartyRU = models.CharField(max_length=200)
    CounterPartyTR = models.CharField(max_length=200)
    CounterPartyINN = models.CharField(max_length=200)
    CounterPartyKPP = models.CharField(max_length=200)
    Client = models.BooleanField(default=False)
    ClientGroup = models.CharField(max_length=100)
    Supplier = models.BooleanField(default=False)

    class Meta:
        ordering = ["CounterPartyEN"]

    def __str__(self):
        return self.CounterPartyEN
    
class Gen_DT_SubjectOfRF(models.Model):
    """Gen_DT_SubjectOfRF"""

    SubjectOfRF_EN = models.CharField(max_length=200)
    SubjectOfRF_RU = models.CharField(max_length=200)
    SubjectOfRF_TR = models.CharField(max_length=200)
    SubjRF_Abbreviation = models.CharField(max_length=200)
    FederalDistrictEN = models.CharField(max_length=200)
    FederalDistrictRU = models.CharField(max_length=200)
    FederalDistrictTR = models.CharField(max_length=200)
    OKATO_CODE = models.CharField(max_length=200)
    
    class Meta:
        ordering = ["SubjectOfRF_EN"]

    def __str__(self):
        return self.SubjectOfRF_EN
    
class Gen_DT_Project(models.Model):
    """Gen_DT_Project"""

    ProjectID_1C = models.CharField(max_length=100)
    ProjectCode = models.CharField(max_length=200)
    ProjectNameEN = models.CharField(max_length=200)
    ProjectNameRU = models.CharField(max_length=200)
    ProjectNameTR = models.CharField(max_length=200)

    SubjectofRF = models.ForeignKey(
        Gen_DT_SubjectOfRF, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Subject of RF"
    )

    AddressEN = models.CharField(max_length=200)
    AddressRU = models.CharField(max_length=200)
    AddressTR = models.CharField(max_length=200)
    StartDate = models.DateField()
    EndDate = models.DateField()
    
    class Meta:
        ordering = ["ProjectNameEN"]

    def __str__(self):
        return self.ProjectNameEN
    

class Gen_DT_CounterPartyType(models.Model):
    """Gen_DT_CounterPartyType"""

    CounterPartyTypeEN = models.CharField(max_length=200)
    CounterPartyTypeRU = models.CharField(max_length=200)
    CounterPartyTypeTR = models.CharField(max_length=200)
    
    class Meta:
        ordering = ["CounterPartyTypeEN"]

    def __str__(self):
        return self.CounterPartyTypeEN
    
class Gen_DT_ContractType(models.Model):
    """Gen_DT_ContractType"""

    ContractTypeEN = models.CharField(max_length=200)
    ContractTypeRU = models.CharField(max_length=200)
    ContractTypeTR = models.CharField(max_length=200)
    
    class Meta:
        ordering = ["ContractTypeEN"]

    def __str__(self):
        return self.ContractTypeEN
    

class Gen_DT_VAT_Rate(models.Model):
    """Gen_DT_VAT_Rate"""

    VAT_Rate = models.IntegerField()
    
    class Meta:
        ordering = ["VAT_Rate"]

    def __str__(self):
        return self.VAT_Rate
    
    
class Gen_DT_UoM(models.Model):
    """Gen_DT_UoM"""

    UoM_Code_1C = models.CharField(max_length=200)
    UoM_Short_EN = models.CharField(max_length=200)
    UoM_Short_RU = models.CharField(max_length=200)
    UoM_Short_TR = models.CharField(max_length=200)
    UoM_EN = models.CharField(max_length=200)
    UoM_RU = models.CharField(max_length=200)
    UoM_TR = models.CharField(max_length=200)
    UoM_Active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ["UoM_Short_EN"]

    def __str__(self):
        return self.UoM_Short_EN
    
class Gen_DT_BudgetData(models.Model):
    """Gen_DT_BudgetData"""

    BudgetVersion = models.IntegerField()
    Discipline = models.ForeignKey(
        Gen_DT_Discipline, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Discipline")

    BudgetCode = models.CharField(max_length=100)
    PrimaveraCode = models.CharField(max_length=100)

    JotTitle = models.ForeignKey(
        Gen_DT_JobTitle, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Job Title")

    LegDocumentType = models.ForeignKey(
        Gen_DT_DocumentType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Document Type")

    Currency = models.ForeignKey(
        Gen_DT_Currency, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Currency")

    UoM = models.ForeignKey(
        Gen_DT_UoM, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="UoM")

    StartOfWorkDate = models.DateField()
    EndOfWorkDate = models.DateField()

    EmpQty = models.IntegerField()
    EmpNetSalary = models.FloatField()

    class Meta:
        #verbose_name =CountryEN "Наименование"
        ordering = ["BudgetVersion"]

    def __str__(self):
        return self.BudgetVersion


class Gen_DT_BudgetDataHistory(models.Model):
    """Gen_DT_BudgetDataHistory"""

    BudgetDate = models.DateField()

    BudgetID = models.ForeignKey(
        Gen_DT_BudgetData, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Budget ID")

    ProjectID = models.ForeignKey(
        Gen_DT_Project, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Project ID")

    
    class Meta:
        ordering = ["BudgetDate"]

    def __str__(self):
        return self.BudgetDate
    
class Gen_DT_ExpenseFrequency(models.Model):
    """Gen_DT_ExpenseFrequency"""

    ExpenseFrequencyEN = models.CharField(max_length=200)
    ExpenseFrequencyRU = models.CharField(max_length=200)
    ExpenseFrequencyTR = models.CharField(max_length=200)
    
    class Meta:
        ordering = ["ExpenseFrequencyEN"]

    def __str__(self):
        return self.ExpenseFrequencyEN
    
class Gen_DT_ExpenseType(models.Model):
    """Gen_DT_ExpenseType"""

    ExpenseTypeEN = models.CharField(max_length=200)
    ExpenseTypeRU = models.CharField(max_length=200)
    ExpenseTypeTR = models.CharField(max_length=200)

    ExpenseFrequency = models.ForeignKey(
        Gen_DT_ExpenseFrequency, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Expense Frequency")

    class Meta:
        ordering = ["ExpenseTypeEN"]

    def __str__(self):
        return self.ExpenseTypeEN
    
class Gen_DT_LegalExpences(models.Model):
    """Gen_DT_LegalExpences"""

    ProjectID = models.ForeignKey(
        Gen_DT_Project, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Project ID")
    
    LegDocumentType = models.ForeignKey(
        Gen_DT_DocumentType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Document Type")
    
    ExpeneseCountry = models.ForeignKey(
        Gen_DT_Country, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Expenese Country")
    
    Currency = models.ForeignKey(
        Gen_DT_Currency, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Currency")
    
    ExpenseType = models.ForeignKey(
        Gen_DT_ExpenseType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Expense Type")
    
    ExpensePrice = models.FloatField()

    LegalExpenseActive = models.BooleanField(default=True)

    EffectiveDate = models.DateField()

    class Meta:
        ordering = ["ProjectID"]

    def __str__(self):
        return self.ProjectID
    
class Gen_DT_EmpLegalStatus(models.Model):
    """Gen_DT_EmpLegalStatus"""

    EmpLegalStatusEN = models.CharField(max_length=200)
    EmpLegalStatusRU = models.CharField(max_length=200)
    EmpLegalStatusTR = models.CharField(max_length=200)

    class Meta:
        ordering = ["EmpLegalStatusEN"]

    def __str__(self):
        return self.EmpLegalStatusEN
    
class Gen_DT_EmpTaxType(models.Model):
    """Gen_DT_EmpTaxType"""

    EmpTaxTypeEN = models.CharField(max_length=200)
    EmpTaxTypeRU = models.CharField(max_length=200)
    EmpTaxTypeTR = models.CharField(max_length=200)

    class Meta:
        ordering = ["EmpTaxTypeEN"]

    def __str__(self):
        return self.EmpTaxTypeEN
    
class Gen_DT_EmpTaxPayer(models.Model):
    """Gen_DT_EmpTaxPayer"""

    EmpTaxCategoryCode = models.CharField(max_length=200)

    EmpTaxCategoryEN = models.CharField(max_length=200)
    EmpTaxCategoryRU = models.CharField(max_length=200)
    EmpTaxCategoryTR = models.CharField(max_length=200)

    EmpTaxType = models.ForeignKey(
        Gen_DT_EmpTaxType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee Tax Type")

    UniformBaseValueLimitUCVB = models.FloatField(verbose_name="UniformBaseValueLimit(UCVB)")
    WithinLimit = models.FloatField()
    AboveLimit = models.FloatField()

    class Meta:
        ordering = ["EmpTaxCategoryEN"]

    def __str__(self):
        return self.EmpTaxCategoryEN
    
class Gen_DT_OurCompany(models.Model):
    """Gen_DT_OurCompany"""

    OurCompanyID_1C = models.CharField(max_length=100)
    OurCompanyEN = models.CharField(max_length=200)
    OurCompanyRU = models.CharField(max_length=200)
    OurCompanyTR = models.CharField(max_length=200)
    OurCompanyINN = models.CharField(max_length=200)
    OurCompanyKPP = models.CharField(max_length=200)
    ShortCode = models.CharField(max_length=100)

    TaxPayer = models.ForeignKey(
        Gen_DT_EmpTaxPayer, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Tax Payer")

    class Meta:
        ordering = ["OurCompanyEN"]

    def __str__(self):
        return self.OurCompanyEN
    
    
class Gen_DT_Contract(models.Model):
    """Gen_DT_Contract"""

    ContractID_1C = models.CharField(max_length=100)
    ContractsNo = models.CharField(max_length=200)
    ContractDate = models.DateField()
    ContractsSubject = models.CharField(max_length=200)

    OurCompany = models.ForeignKey(
        Gen_DT_OurCompany, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Our Company")

    ContractType = models.ForeignKey(
        Gen_DT_ContractType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Contract Type")

    CounterParty = models.ForeignKey(
        Gen_DT_CounterParty, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Counter Party")

    CounterPartyType = models.ForeignKey(
        Gen_DT_CounterPartyType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Counter Party Type")

    Project = models.ForeignKey(
        Gen_DT_Project, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Project")

    Currency = models.ForeignKey(
        Gen_DT_Currency, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Currency")

    ContractAmountVatWo = models.FloatField()

    VAT_Rate = models.ForeignKey(
        Gen_DT_VAT_Rate, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="VAT Rate")

    ContractStartDate = models.DateField()
    ContractEndDate = models.DateField()
    
    class Meta:
        ordering = ["ContractsSubject"]

    def __str__(self):
        return self.ContractsSubject
    
class Gen_DT_EmpTaxCalc(models.Model):
    """Gen_DT_EmpTaxCalc"""

    EmpTaxRateEN = models.CharField(max_length=200)
    EmpTaxRateRU = models.CharField(max_length=200)
    EmpTaxRateTR = models.CharField(max_length=200)

    LegDocumentType = models.ForeignKey(
        Gen_DT_DocumentType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Document Type")

    TaxCodeSSF = models.IntegerField()
    TaxCodePIT_Until182day = models.IntegerField()
    TaxCodePIT_After182day = models.IntegerField()

    class Meta:
        ordering = ["EmpTaxRateEN"]

    def __str__(self):
        return self.EmpTaxRateEN

