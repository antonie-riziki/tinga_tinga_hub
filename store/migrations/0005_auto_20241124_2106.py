# Generated by Django 3.0.5 on 2024-11-24 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20241124_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('applicant_last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('applicant_email', models.EmailField(max_length=254, verbose_name='Email Address')),
                ('applicant_phone_number', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('applicant_address', models.TextField(verbose_name='Address')),
                ('applicant_desired_position', models.CharField(choices=[('operator', 'Tractor Operator'), ('mechanic', 'Tractor Mechanic'), ('technician', 'Field Technician'), ('manager', 'Operations Manager')], max_length=20, verbose_name='Desired Position')),
                ('applicant_years_of_experience', models.PositiveIntegerField(verbose_name='Years of Experience')),
                ('applicant_is_certified_operator', models.BooleanField(default=False, verbose_name='Certified Tractor Operator')),
                ('applicant_certifications', models.TextField(blank=True, null=True, verbose_name='Relevant Certifications')),
                ('applicant_resume', models.FileField(blank=True, null=True, upload_to='resumes/', verbose_name='Upload Resume (PDF or DOC)')),
                ('applicant_cover_letter', models.TextField(blank=True, null=True, verbose_name='Cover Letter')),
                ('applicant_submitted_at', models.DateTimeField(auto_now_add=True, verbose_name='Submitted At')),
            ],
            options={
                'verbose_name': 'Job Application',
                'verbose_name_plural': 'Job Applications',
                'ordering': ['-applicant_submitted_at'],
            },
        ),
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Job Title')),
                ('description', models.TextField(verbose_name='Job Description')),
                ('location', models.CharField(max_length=100, verbose_name='Job Location')),
                ('category', models.CharField(choices=[('operator', 'Tractor Operator'), ('mechanic', 'Tractor Mechanic'), ('technician', 'Field Technician'), ('manager', 'Operations Manager')], max_length=20, verbose_name='Job Category')),
                ('years_of_experience_required', models.PositiveIntegerField(verbose_name='Years of Experience Required')),
                ('certification_required', models.BooleanField(default=False, verbose_name='Certification Required')),
                ('company_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Company Name')),
                ('company_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Contact Email')),
                ('company_phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Contact Phone')),
                ('company_website', models.URLField(blank=True, null=True, verbose_name='Company Website')),
                ('application_deadline', models.DateField(verbose_name='Application Deadline')),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='Posted At')),
            ],
            options={
                'verbose_name': 'Job Posting',
                'verbose_name_plural': 'Job Postings',
                'ordering': ['-posted_at'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50, unique=True, verbose_name='Skill Name')),
            ],
        ),
        migrations.DeleteModel(
            name='Dealer',
        ),
        migrations.DeleteModel(
            name='RepairWorker',
        ),
        migrations.AddField(
            model_name='jobposting',
            name='skills_required',
            field=models.ManyToManyField(blank=True, to='store.Skill', verbose_name='Required Skills'),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='applicant_skills',
            field=models.ManyToManyField(to='store.Skill', verbose_name='Skills and Expertise'),
        ),
    ]