<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class LendingRecord extends Model
{
    //
    protected $guarded = [];

    /**
     * Lending record belongs to a user
     *
     * @return \Illuminate\Database\Eloquent\Relations\BelongsTo
     */
    public function user()
    {
        return $this->belongsTo('App\User');
    }

    /**
     *
     * Lending record belongs to a book
     *
     * @return \Illuminate\Database\Eloquent\Relations\BelongsTo
     */
    public function book()
    {
        return $this->belongsTo('App\Book');
    }
}
