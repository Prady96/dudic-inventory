class State(models.Model):

    id = models.AutoField(
    
    state_name = models.CharField(
        _('State Name'),
        max_length = 46,
        blank = True,
        null = True,
    )
    
    def __str__(self):
        return u'%s' % (self.state_name)
    
class CBSA(models.Model):

    id = models.AutoField(
        primary_key = True
    )
    
    cbsa_title = models.CharField(
        _('CBSA Title'),
        max_length = 46,
        blank = True,
        null = True,
    )
    
    def __str__(self):
        return u'%s' % (self.cbsa_name)


# CBSA/State Connection Table. CBSA's can span several states    
class CBSAState(models.Model):

    id = models.AutoField(
        primary_key = True
    )
    
    state = models.ForeignKey(
        State,
        verbose_name=_('State'),
        on_delete=models.CASCADE,
        null = True,
        blank = True,
    )
    
    cbsa = models.ForeignKey(
        CBSA,
        verbose_name=_('CBSA'),
        on_delete=models.CASCADE,
        null = True,
        blank = True,
    )
    
    def __str__(self):
        return u'%s' % (self.cbsa)
    

    
class econ_writeups(models.Model):

    id = models.AutoField(
        primary_key = True
    )
    
    project_name = models.CharField(
        _('Project Name'),
        max_length = 255,
        blank = True,
        null = True,
        help_text = _('Full name of the project'),
    )
    
    state = models.ForeignKey(
        State,
        verbose_name=_('State'),
        on_delete=models.CASCADE,
        null = True,
        blank = True,
    )
    
    msa = ChainedForeignKey(
        CBSAState,
        chained_field="state",
        chained_model_field="state",
        show_all=True,
        auto_choose=False,
        sort=True,
        verbose_name=_('MSA'),
    )
    
    body_text = models.TextField(
        _('Body of Text'),
        blank=True,
        null=True,
        max_length = 4000,
    )
    
    date_submitted = models.DateTimeField(
        editable = False, 
        auto_now_add = True
    )
    
    def __str__(self):
        return u'%s' % (self.project_name) 