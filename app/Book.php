<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Book extends Model
{
    //
    protected $guarded = [];

    /**
     *
     * Book belongs to a user
     *
     * @return \Illuminate\Database\Eloquent\Relations\BelongsTo
     */
    public function user()
    {
        return $this->belongsTo('App\User');
    }

    /**
     * Book has many lending record
     *
     * @return \Illuminate\Database\Eloquent\Relations\HasMany
     */
    public function lendingRecords()
    {
        return $this->hasMany('App\LendingRecord');
    }

}
