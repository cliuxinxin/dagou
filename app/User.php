<?php

namespace App;

use Illuminate\Notifications\Notifiable;
use Illuminate\Foundation\Auth\User as Authenticatable;

class User extends Authenticatable
{
    use Notifiable;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'name', 'email', 'password',
    ];

    /**
     * The attributes that should be hidden for arrays.
     *
     * @var array
     */
    protected $hidden = [
        'password', 'remember_token',
    ];

    /**
     * User have a profile
     *
     * @return \Illuminate\Database\Eloquent\Relations\HasMany
     */
    public function profiles()
    {
        return $this->hasMany('App\Profile');
    }

    /**
     * User has books
     *
     * @return \Illuminate\Database\Eloquent\Relations\HasMany
     */
    public function books()
    {
        return $this->hasMany('App\Book');

    }


    /**
     * User has many lending records
     *
     * @return \Illuminate\Database\Eloquent\Relations\HasMany
     */
    public function lendingRecords()
    {
        return $this->hasMany('App\LendingRecord');

    }
}
