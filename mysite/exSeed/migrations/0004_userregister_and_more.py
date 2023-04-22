# Generated by Django 4.1.5 on 2023-03-22 16:10

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import exSeed.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exSeed', '0003_alter_userinfo_currentstreak'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spotNiceness', models.PositiveSmallIntegerField(help_text='The number of stars this user has rated the spot upon attendance (1 to 5)', validators=[django.core.validators.MaxValueValidator(5, message='Max rating is 5 stars'), django.core.validators.MinValueValidator(1, message='Min rating is 1 star')])),
                ('registerTime', models.TimeField(auto_now_add=True, help_text='The time that the record is created. Note, this field cannot be edited, and is automatically created', validators=[exSeed.models.valid_time])),
                ('registerTimeEditable', models.TimeField(help_text='An admin, alterable time field for the purposes of testing. Can be null upon record creation', null=True, validators=[exSeed.models.valid_time])),
            ],
            options={
                'verbose_name': 'Entries',
                'verbose_name_plural': 'Register',
            },
        ),
        migrations.RenameField(
            model_name='spot',
            old_name='average_attendance_int',
            new_name='average_attendance',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='group',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='hasTakenPledge',
            field=models.BooleanField(default=False, help_text='Has the user agreed to the Spot of the Day pledge?', verbose_name='Pledged'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='lastSpotRegister',
            field=models.DateField(blank=True, help_text='The date this user last visited a spot', null=True, verbose_name='Last Register Date'),
        ),
        migrations.AlterField(
            model_name='spot',
            name='imageName',
            field=models.CharField(blank=True, help_text='The link to this spots image', max_length=100),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='currentStreak',
            field=models.PositiveSmallIntegerField(blank=True, db_index=True, default=0, help_text='The users current streak', verbose_name='Streak'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='totalPoints',
            field=models.PositiveSmallIntegerField(blank=True, default=0, help_text='The users high score', verbose_name='Points'),
        ),
        migrations.RenameModel(
            old_name='PreviousSpotAttend',
            new_name='SpotRecord',
        ),
        migrations.DeleteModel(
            name='SpotRegister',
        ),
        migrations.AddField(
            model_name='userregister',
            name='srId',
            field=models.ForeignKey(help_text='Related spot-day instance', on_delete=django.db.models.deletion.CASCADE, to='exSeed.spotrecord', verbose_name='Spot data'),
        ),
        migrations.AddField(
            model_name='userregister',
            name='uId',
            field=models.ForeignKey(help_text="This user has attended today's spot", on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
